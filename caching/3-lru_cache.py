#!/usr/bin/env python3
"""
  LRU Caching
"""
import sys
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU caching system that removes the least
    recently used item when the cache limit is reached"""

    def __init__(self):
        """Initialize the LRU cache"""
        super().__init__()  # Call the parent init
        self.key_order = []  # List to track usage order

    def put(self, key, item):
        """Add an item to the cache
           Remove the least recent used item if the cache is full
        """
        if key is None or item is None:
            return

        # If key already exists, remove it to re-insert at the end
        if key in self.cache_data:
            self.key_order.remove(key)
        self.cache_data[key] = item
        self.key_order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Remove the least recently used key
            lru_key = self.key_order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

    def get(self, key):
        """
        Retrieve an item from the cache by key.
        Move the accessed item to the end to mark it as recently used.
        Return None if key is not found.
        """
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed key to the end to mark it as recently used
        self.key_order.remove(key)
        self.key_order.append(key)
        return self.cache_data.get(key)
