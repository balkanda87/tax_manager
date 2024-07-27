#!/usr/bin/env python

__author__ = "Balaji Kandasamy"
__copyright__ = "Copyright 2024, Tax Auditor"
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "someone"
__email__ = "balkanda87@outlook.com"

from pydantic import BaseModel
from typing import List, Optional


# Example database models (use SQLAlchemy or your preferred ORM)
class User(BaseModel):
    user_id: int
    username: str
    email: str
    hashed_password: str


class UserProfile(BaseModel):
    user_details_id: int
    user_id: int
    username: str
    first_name: str
    last_name: str
    mobile_number: str
    pan_id: str
    aadhar_id: str
    uan_id: str
    profile_image: bytes


class UserRole(BaseModel):
    user_role_id: int
    user_id: int
    user_role: str


class Token(BaseModel):
    token_id: int
    user_id: int
    token_type: str
    token: str
    expiration_time: str


class RefreshToken(BaseModel):
    refresh_token_id: int
    user_id: int
    token: str
    expiration_time: str


class PasswordHistory(BaseModel):
    user_id: int
    hashed_password: str
    last_updated: str


class BlackList(BaseModel):
    token_id: int
    blacklisted_at: str


# Generate the Pydantic model from the SQLAlchemy model
# User = sqlalchemy_to_pydantic(User)
