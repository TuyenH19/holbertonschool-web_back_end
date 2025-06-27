#!/usr/bin/env python3
""" Module of auth
"""
from flask import request
from typing import TypeVar


class Auth:
    """ Auth Class - template for all authentication systems"""

    def require_auth(self, path: str, excluded_paths: list[str]) -> bool:
        """ Define which routes don't need authentication """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        if not path.endswith('/'):
            path += '/'

        for ex_path in excluded_paths:
            if ex_path == path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Returns the Authorization header from the request """
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns the current user from the request """
        return None
