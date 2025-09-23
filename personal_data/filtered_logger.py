#!/usr/bin/env python3
"""
Module for filtering and obfuscating log data
"""
import logging
import re
from typing import List


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
