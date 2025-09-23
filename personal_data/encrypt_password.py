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
