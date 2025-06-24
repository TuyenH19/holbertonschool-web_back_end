#!/usr/bin/env python3
""" Module of basic authentication
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """BasicAuth class inherits from Auth """

    def extract_base64_authorization_header(
      self,
      authorization_header: str
    ) -> str:
        """Extract Base64 part of the Authentication header for Basic Auth"""
        if authorization_header is None or \
          not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header[len("Basic "):]
