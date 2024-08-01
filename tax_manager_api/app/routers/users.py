#!/usr/bin/env python

__author__ = "Balaji Kandasamy"
__copyright__ = "Copyright 2024, Tax Auditor"
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "someone"
__email__ = "balkanda87@outlook.com"

import jwt
import datetime
import logging
from fastapi import APIRouter, HTTPException, Depends, HTTPException
from traceback import print_exception
from sqlalchemy.orm import Session
from app.dependencies import get_database_connection, get_password_hash, verify_password
from app.common.token import (
    create_access_token,
    create_refresh_token,
    validate_refresh_token,
    is_token_blacklisted,
    get_token_username,
    get_token_to_blacklist,
    oauth2_scheme,
)
from app.common.constants import HttpClientCode, HttpServerCode, ApiResponse
from app.common.strings import UserMessage, UserErrorMessage, TokenErrorMessage
from app.models.users import (
    UserOrm,
    UserRoleOrm,
    UserProfileOrm,
    TokenOrm,
    Blacklist,
    PasswordHistoryOrm,
)
from app.serdes.users import UserLogin, UserProfile
from app.config.config import Config

uvicorn_access = logging.getLogger("uvicorn.access")
uvicorn_access.disabled = True

logger = logging.getLogger("uvicorn")
logger.setLevel(logging.getLevelName(logging.DEBUG))

users = APIRouter()
tax_config = Config()


# Routes
@users.post("/register")
def register_user(user: UserProfile, db: Session = Depends(get_database_connection)):
    try:
        db_user = (
            db.query(UserProfileOrm).filter(UserProfileOrm.email == user.email).first()
        )
        if db_user:
            raise HTTPException(
                status_code=HttpClientCode.BAD_REQUEST,
                detail=UserErrorMessage.USER_ALREADY_REGISTERED,
            )
        hashed_password = get_password_hash(user.hashed_password)
        db_user = UserProfileOrm(
            username=user.username,
            email=user.email,
            hashed_password=hashed_password,
            first_name=user.first_name,
            last_name=user.last_name,
            mobile_number=user.mobile_number,
            pan_id=user.pan_id,
            aadhar_id=user.aadhar_id,
            uan_id=user.uan_id,
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        db_password_history = (
            db.query(PasswordHistoryOrm)
            .filter(PasswordHistoryOrm.hashed_password == user.hashed_password)
            .first()
        )
        if not db_password_history:
            db_user = (
                db.query(UserProfileOrm)
                .filter(UserProfileOrm.email == user.email)
                .first()
            )
            db_password_history = PasswordHistoryOrm(
                user_details_id=db_user.id,
                hashed_password=hashed_password,
                last_updated=datetime.datetime.now(datetime.UTC),
            )
            db.add(db_password_history)
            db.commit()
        return {
            ApiResponse.MESSAGE: UserMessage.USER_REGISTERED_SUCCESSFULLY,
            "username": db_user.username,
            "email": db_user.email,
        }
    except Exception as e:
        db.rollback()
        print_exception(e)
        logging.error(f"Error registering user: {str(e)}")
        raise HTTPException(
            status_code=HttpServerCode.INTERNAL_SERVER_ERROR,
            detail=f"Error registering user: {str(e)}",
        )
    finally:
        db.close()


@users.post("/token")
def login(user_login: UserLogin, db: Session = Depends(get_database_connection)):
    try:

        db_user = None
        if "@" in user_login.username:
            db_user: UserProfileOrm = (
                db.query(UserProfileOrm)
                .filter(UserProfileOrm.email == user_login.username)
                .first()
            )
        else:
            db_user: UserProfileOrm = (
                db.query(UserProfileOrm)
                .filter(UserProfileOrm.username == user_login.username)
                .first()
            )
        hashed_password = get_password_hash(user_login.password)
        if not db_user or not verify_password(
            user_login.password, db_user.hashed_password
        ):
            raise HTTPException(
                status_code=HttpClientCode.BAD_REQUEST,
                detail=UserErrorMessage.USER_INCORRECT_USER_OR_PASSWORD,
            )
        db_user: UserOrm = (
            db.query(UserOrm).filter(UserOrm.username == db_user.username).first()
        )
        if db_user:
            db_refresh_token: TokenOrm = (
                db.query(TokenOrm)
                .filter(
                    TokenOrm.user_id == db_user.id, TokenOrm.token_type == "refresh"
                )
                .first()
            )
            if db_refresh_token:
                payload = validate_refresh_token(db_refresh_token.token)
                print(payload["exp"])
        user: UserOrm = UserOrm(
            username=user_login.username,
            hashed_password=hashed_password,
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        access_token, expires = create_access_token({"sub": user_login.username})
        refresh_token, expires = create_refresh_token({"sub": user_login.username})
        db_user_role = (
            db.query(UserRoleOrm).filter(UserRoleOrm.user_id == user.id).first()
        )
        if not db_user_role:
            user_role: UserRoleOrm = UserRoleOrm(
                user_id=user.id,
                user_role=user_login.role,
            )

            db.add(user_role)
            db.commit()
        db_token = db.query(TokenOrm).filter(TokenOrm.user_id == user.id).first()
        if not db_token:
            bearer: TokenOrm = TokenOrm(
                user_id=user.id,
                token=access_token,
                token_type="bearer",
                expiration_time=expires,
            )
            refresh: TokenOrm = TokenOrm(
                user_id=user.id,
                token=refresh_token,
                token_type="refresh",
                expiration_time=expires,
            )
            db.add_all((bearer, refresh))
            db.commit()

        return {
            "access_token": access_token,
            "token_type": "bearer",
            "refresh_token": refresh_token,
        }
    except Exception as e:
        db.rollback()
        print_exception(e)
        raise HTTPException(
            status_code=HttpServerCode.INTERNAL_SERVER_ERROR,
            detail=f"Error registering user: {str(e)}",
        )
    finally:
        db.close()


@users.get("/login")
def read_users_me(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(
            token,
            tax_config.tax_app_secert_key,
            algorithms=[tax_config.tax_app_secert_algorithm],
        )
        username = payload.get("sub")
        return {
            "username": username,
            ApiResponse.MESSAGE: UserMessage.USER_LOGGED_IN_SUCCESSFULLY,
        }
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=HttpClientCode.UNAUTHORIZED,
            detail=TokenErrorMessage.TOKEN_EXPIRED,
        )
    except jwt.DecodeError:
        raise HTTPException(
            status_code=HttpClientCode.UNAUTHORIZED,
            detail=TokenErrorMessage.TOKEN_EXPIRED,
        )


@users.delete("/logout")
def logout(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_database_connection)
):
    try:
        refresh_token = get_token_to_blacklist(token)
        if is_token_blacklisted(refresh_token):
            raise HTTPException(
                status_code=HttpClientCode.BAD_REQUEST,
                detail=TokenErrorMessage.TOKEN_ALREADY_BLACKLISTED,
            )
        username = get_token_username(token)
        db_user = db.query(UserOrm).filter(UserOrm.username == username).first()
        if db_user:
            db.query(UserRoleOrm).filter(UserRoleOrm.user_id == db_user.id).delete()
            db.query(TokenOrm).filter(TokenOrm.user_id == db_user.id).delete()
            db.query(UserOrm).filter(UserOrm.username == username).delete()

        db_blacklist = Blacklist(
            token=refresh_token, blacklisted_at=datetime.datetime.now(datetime.UTC)
        )
        db.add(db_blacklist)
        db.commit()
        db.refresh(db_blacklist)
        return {ApiResponse.MESSAGE: UserMessage.USER_LOGGED_OUT_SUCCESSFULLY}
    except Exception as e:
        db.rollback()
        print_exception(e)
        raise HTTPException(
            status_code=HttpServerCode.INTERNAL_SERVER_ERROR,
            detail=f"Error registering user: {str(e)}",
        )
    finally:
        db.close()


@users.get("/protected_data")
def protected_data(token: str = Depends(oauth2_scheme)):
    if is_token_blacklisted(token):
        raise HTTPException(
            status_code=HttpClientCode.UNAUTHORIZED,
            detail=TokenErrorMessage.TOKEN_BLACKLISTED,
        )
    # Your logic to fetch protected data
    return {ApiResponse.MESSAGE: UserMessage.USER_PROTECTED_ACCESS}


@users.get("/users/me")
def read_users_me(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(
            token,
            tax_config.tax_app_secert_key,
            algorithms=[tax_config.tax_app_secert_algorithm],
        )
        username = payload.get("sub")
        return {"username": username}
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=HttpClientCode.UNAUTHORIZED,
            detail=TokenErrorMessage.TOKEN_EXPIRED,
        )
    except jwt.DecodeError:
        raise HTTPException(
            status_code=HttpClientCode.UNAUTHORIZED,
            detail=TokenErrorMessage.TOKEN_EXPIRED,
        )
