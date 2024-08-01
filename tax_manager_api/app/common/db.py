#!/usr/bin/env python

__author__ = "Balaji Kandasamy"
__copyright__ = "Copyright 2024, Tax Auditor"
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "someone"
__email__ = "balkanda87@outlook.com"

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config.config import Config

# Fetches db connection url from tax_config.json
db_url = Config().db_connection_url
print(f"{db_url = }")

# Create an SQLAlchemy session
engine = create_engine(db_url)
SessionLocal = sessionmaker(bind=engine)
# print(f"{SessionLocal().is_active = }")
