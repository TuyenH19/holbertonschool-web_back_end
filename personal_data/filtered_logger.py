#!/usr/bin/env python3
"""
Module for filtering and obfuscating log data
"""
import re


def filter_datum(fields, redaction, message, separator):
    """
    Returns the log message obfuscated
    by replacing field values with redaction string

    Args:
        fields: list of strings representing all fields to obfuscate
        redaction: string representing what the field will be obfuscated with
        message: string representing the log line
        separator: string representing the character
        separating fields in the log line

    Returns:
        The obfuscated log message
    """
    pattern = f"({'|'.join(fields)})=([^{re.escape(separator)}]*)"
    return re.sub(pattern, rf"\1={redaction}", message)
