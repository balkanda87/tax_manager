#!/usr/bin/env python

__author__ = "Balaji Kandasamy"
__copyright__ = "Copyright 2024, Tax Auditor"
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "someone"
__email__ = "balkanda87@outlook.com"

import json
import os


class Config:
    def __init__(self) -> None:
        # self.tax_manager_file_path = ""
        # self.db_connection_url = ""
        # self.tax_app_secert_key = ""
        # self.tax_app_secert_algorithm = ""
        # self.access_token_expiry_minutes = ""

        # def fetch_config_params(self):
        with open(
            os.getcwd() + "/tax_manager_api/config/tax_config.json",
            "r",
            encoding="utf-8",
        ) as tax_config:
            json_data = json.load(tax_config)
        if (
            "tax_manager_api" in json_data
            and "logfilepath"
            and json_data["tax_manager_api"]
        ):
            self.tax_manager_file_path = json_data["tax_manager_api"]["logfilepath"]
        if "tax_manager_api" in json_data and "db_url" and json_data["tax_manager_api"]:
            self.db_connection_url = json_data["tax_manager_api"]["db_url"]
        if (
            "tax_manager_api" in json_data
            and "secret_key"
            and json_data["tax_manager_api"]
        ):
            self.tax_app_secert_key = json_data["tax_manager_api"]["secret_key"]
        if (
            "tax_manager_api" in json_data
            and "algorithm"
            and json_data["tax_manager_api"]
        ):
            self.tax_app_secert_algorithm = json_data["tax_manager_api"]["algorithm"]
        if (
            "tax_manager_api" in json_data
            and "access_token_expire_minutes"
            and json_data["tax_manager_api"]
        ):
            self.access_token_expiry_minutes = json_data["tax_manager_api"][
                "access_token_expire_minutes"
            ]

        if (
            "tax_manager_api" in json_data
            and "refresh_token_expire_days"
            and json_data["tax_manager_api"]
        ):
            self.refresh_token_expire_days = json_data["tax_manager_api"][
                "refresh_token_expire_days"
            ]
