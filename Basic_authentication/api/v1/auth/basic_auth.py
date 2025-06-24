#!/usr/bin/env python3
""" Module of basic authentication
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """BasicAuth class inherits from Auth """

    def extract_base64_authorization_header(
      self,
      authorization_header: str
    ) -> str:
        """Extract Base64 part of the Authentication header for Basic Auth"""
        if (
          authorization_header is None
          or not isinstance(authorization_header, str)
        ):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header[len("Basic "):]

    def decode_base64_authorization_header(
      self,
      base64_authorization_header: str
    ) -> str:
        """Extract Base64 decode of the Authentication header for Basic Auth"""
        if (
            base64_authorization_header is None
            or not isinstance(base64_authorization_header, str)
        ):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            return None
