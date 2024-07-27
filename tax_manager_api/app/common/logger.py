#!/usr/bin/env python

__author__ = "Balaji Kandasamy"
__copyright__ = "Copyright 2024, Tax Auditor"
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "someone"
__email__ = "balkanda87@outlook.com"

import logging
from app.config.config import Config
from logging.handlers import RotatingFileHandler


# Add color to log levels
class ColoredFormatter(logging.Formatter):
    COLORS = {
        "DEBUG": "\033[30m",  # Black
        "INFO": "\033[32m",  # Green
        "WARNING": "\033[33m",  # Orange/Yellow
        "ERROR": "\033[31m",  # Red
        "CRITICAL": "\033[31m",  # Red
    }

    def format(self, record):
        log_level = record.levelname
        colored_log_level = f"{self.COLORS.get(log_level, '')}{log_level}\033[0m"
        record.levelname = colored_log_level
        return super().format(record)


# Configure logging
tax_config = Config()
tax_config.fetch_config_params()
log_formatter = ColoredFormatter(
    "[%(asctime)s] [%(levelname)s] [%(pathname)s:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Create a rotating file handler (max 1 MB, keep 3 backups)
file_handler = RotatingFileHandler(
    tax_config.tax_manager_file_path, maxBytes=1e6, backupCount=3
)
file_handler.setFormatter(log_formatter)

# Set log level (adjust as needed)
file_handler.setLevel(logging.DEBUG)

# Add the handler to the root logger
logging.root.addHandler(file_handler)
