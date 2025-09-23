#!/usr/bin/env python3
"""
Utilities for redacting personally identifiable information (PII) from logs.

Exposes:
- filter_datum: single-regex helper to obfuscate field values in messages.
- RedactingFormatter: logging.Formatter that applies filter_datum.
- PII_FIELDS: tuple of key PII field names to redact.
- get_logger: configured Logger named "user_data".
"""
import logging
import re
from typing import List, Tuple

# Five “important” PII fields present in user_data.csv
PII_FIELDS: Tuple[str, ...] = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Redact specified field values in a delimited message."""
    fld = "|".join(map(re.escape, fields))
    sep = re.escape(separator)
    return re.sub(rf'({fld})=[^{sep}]*', r'\1=' + redaction, message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initialize the formatter with fields to redact"""
        super().__init__(self.FORMAT)
        self.fields = list(fields)

    def format(self, record: logging.LogRecord) -> str:
        """Format the log record, redacting specified fields"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def get_logger() -> logging.Logger:
    """
    Create and return a configured logger named 'user_data'.

    - Level: INFO (do not emit DEBUG)
    - No propagation to ancestor loggers
    - StreamHandler with RedactingFormatter using PII_FIELDS
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # Avoid duplicate handlers if called multiple times
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
        logger.addHandler(handler)

    return logger
