#!/usr/bin/env python3
"""
Password hashing utilities.

Exposes:
- hash_password: return a salted bcrypt hash for a given plaintext password.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Return a salted, hashed password as bytes using bcrypt."""
    if not isinstance(password, str):
        raise TypeError("password must be a string")
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Return True if `password` matches `hashed_password` via bcrypt."""
    if not isinstance(hashed_password, (bytes, bytearray)):
        raise TypeError("hashed_password must be bytes-like")
    if not isinstance(password, str):
        raise TypeError("password must be a string")
    return bcrypt.checkpw(password.encode("utf-8"), bytes(hashed_password))
