#!/usr/bin/env python

__author__ = "Balaji Kandasamy"
__copyright__ = "Copyright 2024, Tax Auditor"
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "someone"
__email__ = "balkanda87@outlook.com"

import os


class HttpValidation:
    def __init__(self) -> None:
        pass


class FileValidation:
    def __init__(self) -> None:
        pass

    @staticmethod
    def is_file_exist(filepath):
        """function is_file_exist checks if file exist in the path or not"""
        return os.path.exists(filepath)

    @staticmethod
    def is_file_empty(filepath):
        """function is_file_empty checks if file exist in the path or not"""
        return os.stat(filepath).st_size == 0

    @staticmethod
    def has_extention(filepath, extention):
        """function is_file_empty checks if file exist in the path or not"""
        if filepath:
            if "." in filepath and filepath.split(".")[-1] == extention.strip():
                return True
        return False


class AwsValidation:
    def __init__(self) -> None:
        pass
