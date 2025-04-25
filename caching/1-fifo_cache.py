#!/usr/bin/env python3
"""
  FIFO Caching
"""
import sys
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching system that removes
    the oldest item when the cache limit is reached"""

    def __init__(self):
        """Initialize the FIFO cache"""
        super().__init__()  # Call the parent init
        self.order = []  # List to track insertion order

    def put(self, key, item):
        """Add an item to the cache
           Remove the oldest item if the cache is full
        """
        if key is None or item is None:
            return

        if (
            key not in self.cache_data
            and len(self.cache_data) >= BaseCaching.MAX_ITEMS
        ):
            # Remove the oldest key
            oldest_key = self.order.pop(0)
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")

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
