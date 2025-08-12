#!/usr/bin/env python3
"""
Redis basic
"""
import uuid
import redis


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
