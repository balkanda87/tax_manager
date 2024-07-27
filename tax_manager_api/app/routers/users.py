#!/usr/bin/env python

__author__ = "Balaji Kandasamy"
__copyright__ = "Copyright 2024, Tax Auditor"
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "someone"
__email__ = "balkanda87@outlook.com"

import jwt
from fastapi import APIRouter, HTTPException, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from typing import List
from serdes.users import User
from app.common.token import create_access_token, oauth2_scheme
from app.common.constants import HttpClientCode
from app.config.config import Config

users = APIRouter()
tax_config = Config()

# Example user data (replace with your actual user data)
fake_users_db = {
    "user@example.com": {
        "username": "user",
        "hashed_password": "hashedpassword",
    }
}


# Routes
@users.post("/token")
def login(form_data: OAuth2PasswordRequestForm):
    user = fake_users_db.get(form_data.username)
    if not user or user["hashed_password"] != form_data.password:
        raise HTTPException(
            status_code=HttpClientCode.BAD_REQUEST,
            detail="Incorrect username or password",
        )
    access_token = create_access_token({"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}


@users.get("/login")
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
            status_code=HttpClientCode.UNAUTHORIZED, detail="Token has expired"
        )
    except jwt.DecodeError:
        raise HTTPException(
            status_code=HttpClientCode.UNAUTHORIZED, detail="Invalid token"
        )


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
            status_code=HttpClientCode.UNAUTHORIZED, detail="Token has expired"
        )
    except jwt.DecodeError:
        raise HTTPException(
            status_code=HttpClientCode.UNAUTHORIZED, detail="Invalid token"
        )


# Example routes
@users.post("/users/", response_model=List[User])
def create_user(user: User):
    # Logic to create a new user in the database
    # Return the created user
    return user


@users.get("/users/{user_id}", response_model=User)
def read_user(user_id: int):
    # Logic to retrieve a user by user_id
    # Return the user
    return {"user_id": user_id, "username": "example"}


@users.put("/users/{user_id}", response_model=User)
def read_user(user_id: int):
    # Logic to retrieve a user by user_id
    # Return the user
    return {"user_id": user_id, "username": "example"}


@users.post("/users/{user_id}", response_model=User)
def read_user(user_id: int):
    # Logic to retrieve a user by user_id
    # Return the user
    return {"user_id": user_id, "username": "example"}


@users.delete("/users", response_model=User)
def read_user(user_id: int):
    # Logic to retrieve a user by user_id
    # Return the user
    return {"user_id": user_id, "username": "example"}
