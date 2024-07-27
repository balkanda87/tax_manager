#!/usr/bin/env python

__author__ = "Balaji Kandasamy"
__copyright__ = "Copyright 2024, Tax Auditor"
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "someone"
__email__ = "balkanda87@outlook.com"

from sqlalchemy import Column, Integer, String, TIMESTAMP, LargeBinary
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    hashed_password = Column(String(255), nullable=False)


class UserProfile(Base):
    __tablename__ = "user_profile"

    user_details_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    username = Column(String(100), nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(10), nullable=False)
    mobile_number = Column(String(18), nullable=False)
    pan_id = Column(String(18), nullable=True)
    aadhar_id = Column(String(18), nullable=True)
    uan_id = Column(String(18), nullable=True)
    profile_image = Column(LargeBinary, nullable=True)


class UserRole(Base):
    __tablename__ = "user_role"

    user_role_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    user_role = Column(String(100), nullable=False)


class Token(Base):
    __tablename__ = "tokens"

    token_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    token = Column(String(255), nullable=False)
    token_type = Column(String(10), nullable=False)
    expiration_time = Column(TIMESTAMP, nullable=False)


class RefreshToken(Base):
    __tablename__ = "refresh_tokens"

    refresh_token_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    token = Column(String(255), nullable=False)
    expiration_time = Column(TIMESTAMP, nullable=False)


class PasswordHistory(Base):
    __tablename__ = "password_history"

    user_id = Column(Integer, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    last_updated = Column(TIMESTAMP, nullable=False)


class Blacklist(Base):
    __tablename__ = "blacklist"

    token_id = Column(Integer, nullable=False)
    blacklisted_at = Column(TIMESTAMP, nullable=False)
