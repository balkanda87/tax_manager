#!/usr/bin/env python

__author__ = "Balaji Kandasamy"
__copyright__ = "Copyright 2024, Tax Auditor"
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "someone"
__email__ = "balkanda87@outlook.com"

from sqlalchemy import Column, Integer, String, TIMESTAMP, LargeBinary, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UserOrm(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    hashed_password = Column(String(255), nullable=False)


class UserProfileOrm(Base):
    __tablename__ = "user_profile"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), nullable=False)
    hashed_password = Column(String(255), nullable=False)
    email = Column(String(100), nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    mobile_number = Column(String(18), nullable=False)
    pan_id = Column(String(18), nullable=True)
    aadhar_id = Column(String(18), nullable=True)
    uan_id = Column(String(50), nullable=True)
    profile_image = Column(LargeBinary, nullable=True)  # Store profile image as bytes


class UserRoleOrm(Base):
    __tablename__ = "user_role"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user_role = Column(String(100), nullable=False)


class TokenOrm(Base):
    __tablename__ = "tokens"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    token = Column(String(255), nullable=False)
    token_type = Column(String(10), nullable=False)
    expiration_time = Column(TIMESTAMP, nullable=False)


class RefreshTokenOrm(Base):
    __tablename__ = "refresh_tokens"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    token = Column(String(255), nullable=False)
    expiration_time = Column(TIMESTAMP, nullable=False)


class PasswordHistoryOrm(Base):
    __tablename__ = "password_history"

    id = Column(Integer, primary_key=True)
    user_details_id = Column(Integer, ForeignKey("user_profile.id"), nullable=False)
    hashed_password = Column(String(255), nullable=False)
    last_updated = Column(TIMESTAMP, nullable=False)


class Blacklist(Base):
    __tablename__ = "blacklist"

    id = Column(Integer, primary_key=True)
    refresh_token_id = Column(Integer, ForeignKey("refresh_token.id"), nullable=False)
    blacklisted_at = Column(TIMESTAMP, nullable=False)
