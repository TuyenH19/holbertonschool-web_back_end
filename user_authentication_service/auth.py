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


def _generate_uuid() -> str:
    """Return a new UUID as a string (module-private helper)."""
    return str(uuid4())


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

    def create_session(self, email: str) -> Optional[str]:
        """Create a session for the user and return the session id;
        None if user not found."""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None

        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: Optional[str]):
        """Return the User corresponding to the given session_id, or None."""
        if session_id is None:
            return None
        try:
            return self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Invalidate the user's session by clearing session_id."""
        if user_id is None:
            return None
        try:
            # Only use public DB methods
            self._db.update_user(user_id, session_id=None)
        except ValueError:
            # User not found or invalid field — do nothing per spec
            pass
        return None

    def get_reset_password_token(self, email: str) -> str:
        """Generate a reset token for the user identified by email."""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError("User does not exist")

        token = _generate_uuid()
        self._db.update_user(user.id, reset_token=token)
        return token

    def update_password(self, reset_token: str, password: str) -> None:
        """
        Update a user's password using a valid reset_token.
        - If reset_token is unknown, raise ValueError.
        - If not, hash new password, update user, and clear reset_token.
        """
        if not reset_token:
            raise ValueError("Invalid reset token")

        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError("Invalid reset token")

        new_hash = _hash_password(password)  # bytes
        # Our model stores hashed_password as String, so decode to str
        self._db.update_user(user.id, hashed_password=new_hash.decode("utf-8"),
                             reset_token=None)
        return None
