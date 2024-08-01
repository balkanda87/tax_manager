#!/usr/bin/env python

__author__ = "Balaji Kandasamy"
__copyright__ = "Copyright 2024, Tax Auditor"
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "someone"
__email__ = "balkanda87@outlook.com"

import logging
from fastapi import Depends, HTTPException
from passlib.context import CryptContext
from app.common.db import SessionLocal


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


async def common_parameters(q: str = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


def get_database_connection():
    db = SessionLocal()
    logging.info(f"{db.info}")
    try:
        yield db
    finally:
        db.close()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


class FixedContentQueryChecker:
    def __init__(self, fixed_content: str):
        self.fixed_content = fixed_content

    def __call__(self, query: str = ""):
        if query:
            return self.fixed_content in query
        return False


checker = FixedContentQueryChecker("")

# Usage example:
# user = db.query(models.User).filter(models.User.email == email).first()
# if not user or not verify_password(password, user.hashed_password):
# Invalid credentials


# def authenticate_user(token: str = Depends(get_token_from_header)):
#    user = decode_token(token)
#    if not user:
#        raise HTTPException(status_code=401, detail="Unauthorized")
#    return user


# def check_user_permissions(user: User = Depends(authenticate_user)):
#    if not user.has_permission("read_items"):
#        raise HTTPException(status_code=403, detail="Insufficient permissions")
#    return user
