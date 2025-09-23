#!/usr/bin/env python3
"""
Utilities for redacting personally identifiable information (PII) from logs
and connecting to a secured MySQL database using environment variables, and
emitting redacted rows from the `users` table.
"""
import logging
import re
import os
from typing import List, Tuple

import mysql.connector
from mysql.connector.connection import MySQLConnection

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


def get_db() -> MySQLConnection:
    """
    Create and return a MySQL database connector using environment variables.

    Environment variables:
        PERSONAL_DATA_DB_USERNAME (default: "root")
        PERSONAL_DATA_DB_PASSWORD (default: "")
        PERSONAL_DATA_DB_HOST     (default: "localhost")
        PERSONAL_DATA_DB_NAME     (no default; must be set)

    Returns:
        mysql.connector.connection.MySQLConnection: an open DB connection.
    """
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    database = os.getenv("PERSONAL_DATA_DB_NAME")

    return mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=database,
    )


def main() -> None:
    """
    Connect to the DB and print all users with PII fields redacted.

    Output format (handled by the logger's formatter):
    [HOLBERTON] user_data INFO YYYY-mm-dd HH:MM:SS,ms: name=***; email=***; ...
    """
    db = get_db()
    cursor = db.cursor()
    logger = get_logger()

    try:
        query = (
            "SELECT name, email, phone, ssn, password, ip, "
            "last_login, user_agent FROM users;"
        )
        cursor.execute(query)

        for (
            name, email, phone, ssn, password,
            ip, last_login, user_agent
        ) in cursor:
            message = (
                f"name={name}; email={email}; phone={phone}; ssn={ssn}; "
                f"password={password}; ip={ip}; last_login={last_login}; "
                f"user_agent={user_agent};"
            )
            logger.info(message)
    finally:
        cursor.close()
        db.close()


if __name__ == "__main__":
    main()
