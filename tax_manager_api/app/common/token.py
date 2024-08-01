#!/usr/bin/env python

__author__ = "Balaji Kandasamy"
__copyright__ = "Copyright 2024, Tax Auditor"
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "someone"
__email__ = "balkanda87@outlook.com"


import jwt
from fastapi import APIRouter, Header, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta, UTC
from sqlalchemy.orm import Session
from app.dependencies import get_database_connection
from app.config.config import Config
from app.common.strings import TokenErrorMessage, UserErrorMessage
from app.common.constants import HttpClientCode
from app.models.users import Blacklist, TokenOrm, UserOrm
from app.common.constants import HttpClientCode
from app.common.strings import TokenErrorMessage

app = APIRouter()


# OAuth2 password bearer flow
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")
tax_config = Config()


# Generate access token
def create_access_token(data: dict):
    expires = datetime.now(UTC) + timedelta(
        minutes=tax_config.access_token_expiry_minutes
    )
    return (
        jwt.encode(
            {"exp": expires, **data},
            tax_config.tax_app_secert_key,
            algorithm=tax_config.tax_app_secert_algorithm,
        ),
        expires,
    )


# Generate refresh token
def create_refresh_token(user_id: int):
    expires = datetime.now(UTC) + timedelta(days=tax_config.refresh_token_expire_days)
    payload = {"sub": user_id, "exp": expires}
    refresh_token = jwt.encode(
        payload,
        tax_config.tax_app_secert_key,
        algorithm=tax_config.tax_app_secert_algorithm,
    )
    return refresh_token, expires


async def validate_refresh_token(refresh_token: str):
    try:
        payload = jwt.decode(
            refresh_token,
            tax_config.tax_app_secert_key,
            algorithms=[tax_config.tax_app_secert_algorithm],
        )
        if payload["sub"] != "refresh":
            raise jwt.PyJWKError(TokenErrorMessage.TOKEN_INVALID)
        # Handle other validation checks if needed
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=HttpClientCode.UNAUTHORIZED,
            detail=TokenErrorMessage.TOKEN_EXPIRED_TYPE_REFRESH,
        )


# Fetch token from HTTP header
def get_token_from_header(authorization: str = Header(...)):
    try:
        scheme, token = authorization.split()
        if scheme.lower() != "bearer":
            raise HTTPException(
                status_code=HttpClientCode.UNAUTHORIZED,
                detail=UserErrorMessage.USER_INVALID_AUTHENTICATION_SCHEME,
            )
        return token
    except ValueError:
        raise HTTPException(
            status_code=HttpClientCode.UNAUTHORIZED,
            detail=UserErrorMessage.USER_INVALID_AUTHENTICATION_HEADER,
        )


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


def is_token_blacklisted(token: str, db: Session = Depends(get_database_connection)):
    db_user: Blacklist = db.query(Blacklist).filter_by(token).first()
    if not db_user:
        raise HTTPException(
            status_code=HttpClientCode.UNAUTHORIZED,
            detail=TokenErrorMessage.TOKEN_BLACKLISTED,
        )
    return True


def get_token_username(token: str):
    payload = jwt.decode(
        token,
        tax_config.tax_app_secert_key,
        algorithms=[tax_config.tax_app_secert_algorithm],
    )
    username = payload.get("sub")
    return username


def get_token_to_blacklist(token: str, db: Session = Depends(get_database_connection)):
    payload = jwt.decode(
        token,
        tax_config.tax_app_secert_key,
        algorithms=[tax_config.tax_app_secert_algorithm],
    )
    username = payload.get("sub")
    db_user: UserOrm = db.query(UserOrm).filter_by(username).first()
    db_token: TokenOrm = (
        db.query(TokenOrm)
        .filter(TokenOrm.user_id == db_user.id, TokenOrm.token_type == "refresh")
        .first()
    )
    if not db_token:
        raise HTTPException(
            status_code=HttpClientCode.UNAUTHORIZED,
            detail=TokenErrorMessage.TOKEN_BLACKLISTED,
        )
    return db_token.token


# Add middleware to validate tokens
# @users.middleware("http")
async def validate_token(request, call_next):
    token = request.headers.get("Authorization", "").split(" ")[1]
    if is_token_blacklisted(token):
        raise HTTPException(
            status_code=HttpClientCode.UNAUTHORIZED,
            detail=TokenErrorMessage.TOKEN_BLACKLISTED,
        )
    response = await call_next(request)
    return response
