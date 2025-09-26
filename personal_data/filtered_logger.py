#!/usr/bin/env python3
"""
filtered_logger module.
"""
import re
from typing import List
import logging
import os
import mysql.connector

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ RedactingFormatter class constructor."""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ RedactingFormatter class format method."""
        record.msg = filter_datum(
            self.fields,
            self.REDACTION,
            record.getMessage(),
            self.SEPARATOR
        )
        return super().format(record)


def filter_datum(
    fields: List[str],
    redaction: str,
    message: str,
    separator: str
) -> str:
    """
    Returns the log message obfuscated.

    Args:
        fields: A list of strings representing all fields to obfuscate
        redaction: A string representing by what the field will be obfuscated
        message: A string representing the log line
        separator: A string representing the separator

    Returns:
        The log message with specified fields obfuscated
    """
    for field in fields:
        message = re.sub(
            f"{field}=[^{separator}]+",
            f"{field}={redaction}",
            message
        )
    return message


def get_logger() -> logging.Logger:
    """
    Returns a logging.Logger object.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))

    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Returns a mysql.connector.connection.MySQLConnection object.
    """
    try:
        return mysql.connector.connect(
            host=os.getenv("PERSONAL_DATA_DB_HOST", "localhost"),
            database=os.getenv("PERSONAL_DATA_DB_NAME", "my_db"),
            user=os.getenv("PERSONAL_DATA_DB_USERNAME", "root"),
            password=os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
        )
    except mysql.connector.Error as err:
        logger = get_logger()
        logger.error(f"Database connection failed: {err}")
        return None


def main():
    """Obtain a database connection using get_db
    and retrieve all rows in the users table"""
    logger = get_logger()
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users")
    data = cur.fetchall()

    columns = [col[0] for col in cur.description]
    for row in data:
        formatted_row = "; ".join([f"{col}={val}"
                                   for col, val in zip(columns, row)])
        logger.info(formatted_row)

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
