#!/usr/bin/env python3
"""Authentication helpers"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """Return a salted bcrypt hash of the input password as bytes."""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
