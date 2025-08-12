#!/usr/bin/env python3
"""
Redis basic
"""
import uuid
import redis
from functools import wraps
from typing import Callable, Optional, TypeVar, Union, Any


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts how many times `method` is called, using Redis INCR.
    Uses the wrapper's qualified name so it matches what callers read via
    `cache.store.__qualname__`.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # self is the Cache instance; bump the counter in Redis
        key = wrapper.__qualname__  # robust: matches cache.store.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """Simple Redis cache class"""

    def __init__(self):
        """
        Store an instance of redis client and flush it.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
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
        fn: Optional[Callable[[bytes], Any]] = None,
    ) -> Optional[Any]:
        """
        Retrieve a value by key.
        If `fn` is provided, convert the raw bytes with it.
        Preserve Redis behavior: return None if key doesn't exist.
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
