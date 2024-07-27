#!/usr/bin/env python

__author__ = "Balaji Kandasamy"
__copyright__ = "Copyright 2024, Tax Auditor"
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "someone"
__email__ = "balkanda87@outlook.com"


import jwt
from fastapi import APIRouter, Header, HTTPException
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from app.config.config import Config

app = APIRouter()


# OAuth2 password bearer flow
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")
tax_config = Config()


# Generate access token
def create_access_token(data: dict):
    expires = datetime.now(datetime.UTC) + timedelta(
        minutes=tax_config.access_token_expiry_minutes
    )
    return jwt.encode(
        {"exp": expires, **data},
        tax_config.tax_app_secert_key,
        algorithm=tax_config.tax_app_secert_algorithm,
    )


# Generate refresh token
def create_refresh_token(user_id: int):
    expires = datetime.now(datetime.UTC) + timedelta(
        days=tax_config.refresh_token_expire_days
    )
    payload = {"sub": user_id, "exp": expires}
    refresh_token = jwt.encode(
        payload,
        tax_config.tax_app_secert_key,
        algorithm=tax_config.tax_app_secert_algorithm,
    )
    return refresh_token


# Fetch token from HTTP header
def get_token_from_header(authorization: str = Header(...)):
    try:
        scheme, token = authorization.split()
        if scheme.lower() != "bearer":
            raise HTTPException(status_code=401, detail="Invalid authentication scheme")
        return token
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid authorization header")


class TokenBlacklist:
    def __init__(self):
        self.blacklisted_tokens = set()

    def blacklist_token(self, token):
        self.blacklisted_tokens.add(token)

    def is_token_blacklisted(self, token):
        return token in self.blacklisted_tokens


blacklist = TokenBlacklist()

# Blacklist a token (e.g., when a user logs out)
token_to_blacklist = "my_refresh_token"
blacklist.blacklist_token(token_to_blacklist)

# Check if a token is blacklisted
if blacklist.is_token_blacklisted(token_to_blacklist):
    print(f"Token '{token_to_blacklist}' is blacklisted.")
else:
    print(f"Token '{token_to_blacklist}' is not blacklisted.")
