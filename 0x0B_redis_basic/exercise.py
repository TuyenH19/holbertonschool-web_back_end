#!/usr/bin/env python3
"""
Redis basic
"""
import uuid
import redis
from typing import Callable, Optional, TypeVar, Union


class Cache:
    """Simple Redis cache class"""

    def __init__(self):
        """
        Store an instance of redis client and flush it.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data):
        """
        Generate a random key and store input in Redis.
        Args:
            data: Data to store in Redis.
        Returns:
            The key of the stored data.
        """
        key = str(uuid.uuid1())
        self._redis.set(key, data)
        return key

    def get(
        self,
        key: str,
        fn: Optional[Callable[[bytes], T]] = None,
    ) -> Optional[Union[bytes, T]]:
        """
        Retrieve a value by key. If `fn` is provided, use it to convert the
        raw bytes to a desired type. Preserve Redis behavior: return None
        if the key does not exist.

        Args:
            key: Redis key to fetch.
            fn: Optional converter that accepts bytes and returns T.

        Returns:
            bytes if no converter is given; otherwise T. Returns None if
            the key doesn't exist.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve a UTF-8 string value (or None if missing)."""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve an integer value (or None if missing)."""
        return self.get(key, fn=int)
