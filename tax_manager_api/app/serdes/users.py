#!/usr/bin/env python

__author__ = "Balaji Kandasamy"
__copyright__ = "Copyright 2024, Tax Auditor"
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "someone"
__email__ = "balkanda87@outlook.com"

from uuid import uuid4
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from typing import Optional


users = APIRouter()


# Example database models (use SQLAlchemy or your preferred ORM)
class UserLogin(BaseModel):
    # id: Optional[int] = Field(default_factory=lambda: uuid4().hex)
    username: str
    role: str
    password: str


class UserProfile(BaseModel):
    # id: Optional[int] = Field(default_factory=lambda: uuid4().hex)
    username: str
    hashed_password: str
    email: str
    first_name: str
    last_name: str
    mobile_number: str
    pan_id: Optional[str] = None
    aadhar_id: Optional[str] = None
    uan_id: Optional[str] = None
    profile_image: Optional[bytes] = None


class TokenData(BaseModel):
    token_id: int
    user_id: int
    token_type: str
    token: str
    expiration_time: str


class PasswordHistory(BaseModel):
    hashed_password: str
    last_updated: str


class BlackListData(BaseModel):
    token_id: int
    blacklisted_at: str


# Generate the Pydantic model from the SQLAlchemy model
# User = sqlalchemy_to_pydantic(User)
