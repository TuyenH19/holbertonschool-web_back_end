#!/usr/bin/env python3
""" Module of auth
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth Class - template for all authentication systems"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Determines if authentication is required """
        return False

    def authorization_header(self, request=None) -> str:
        """ Returns the Authorization header from the request """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns the current user from the request """
        return None
