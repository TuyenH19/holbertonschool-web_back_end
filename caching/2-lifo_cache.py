#!/usr/bin/env python3
"""
  LIFO Caching
"""
import sys
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching system that removes the latest item when the cache limit is reached"""

    def __init__(self):
        """Initialize the LIFO cache"""
        super().__init__()  # Call the parent init
        self.order = []  # List to track insertion order

    def put(self, key, item):
        """Add an item to the cache
           Remove the latest item if the cache is full
        """
        if key is None or item is None:
            return

        if key not in self.cache_data and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Remove the latest key
            latest_key = self.order.pop()
            del self.cache_data[latest_key]
            print(f"DISCARD: {latest_key}")

        # If key already exists, remove it to re-insert at the end
        if key in self.order:
            self.order.remove(key)

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache by key.
        Return None if key is not found.
        """
        return self.cache_data.get(key, None)
