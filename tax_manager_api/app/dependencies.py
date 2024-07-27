#!/usr/bin/env python

__author__ = "Balaji Kandasamy"
__copyright__ = "Copyright 2024, Tax Auditor"
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "someone"
__email__ = "balkanda87@outlook.com"


from fastapi import Depends, HTTPException
from app.common.token import get_token_from_header


async def common_parameters(q: str = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


class FixedContentQueryChecker:
    def __init__(self, fixed_content: str):
        self.fixed_content = fixed_content

    def __call__(self, q: str = ""):
        if q:
            return self.fixed_content in q
        return False


checker = FixedContentQueryChecker("")


def get_database_connection():
    pass
    # return get_db_connection()


# def authenticate_user(token: str = Depends(get_token_from_header)):
#    user = decode_token(token)
#    if not user:
#        raise HTTPException(status_code=401, detail="Unauthorized")
#    return user


# def check_user_permissions(user: User = Depends(authenticate_user)):
#    if not user.has_permission("read_items"):
#        raise HTTPException(status_code=403, detail="Insufficient permissions")
#    return user
