#!/usr/bin/env python3
"""Authentication helpers"""

from typing import Optional
import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4

from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """Return a salted bcrypt hash of the input string password as bytes."""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self) -> None:
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user.
        - If a user with the given email exists, raise:
            ValueError("User <email> already exists")
        - Otherwise, hash the password, create and return the User.
        """
        try:
            # Will raise NoResultFound if the user doesn't exist
            self._db.find_user_by(email=email)
            # If we get here, a user exists → raise ValueError
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            # Safe to create the user
            hashed = _hash_password(password)  # bytes
            # Our model stores hashed_password as String, so decode to str
            return self._db.add_user(email, hashed.decode("utf-8"))

    def valid_login(self, email: str, password: str) -> bool:
        """Validate credentials for a user."""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False

        # stored hash is a str (from earlier tasks), bcrypt needs bytes
        stored_hash = (user.hashed_password or "").encode("utf-8")
        plain = password.encode("utf-8")

        try:
            return bcrypt.checkpw(plain, stored_hash)
        except ValueError:
            # if stored_hash is malformed for any reason
            return False

    def _generate_uuid() -> str:
        """Return a new UUID as a string (module-private helper)."""
        return str(uuid4())
