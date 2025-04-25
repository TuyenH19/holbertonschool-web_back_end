#!/usr/bin/env python3
"""
  MRU Caching
"""
import sys
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU caching system that removes the most
    recently used item when the cache limit is reached"""

    def __init__(self):
        """Initialize the MRU cache"""
        super().__init__()  # Call the parent init
        self.order = []  # List to track usage order

    def put(self, key, item):
        """Add an item to the cache
           Remove the most recently used item if the cache is full
        """
        if key is None or item is None:
            return

        # If the cache is full and the key is not already in the cache
        if (key not in self.cache_data
            and len(self.cache_data) >= BaseCaching.MAX_ITEMS):
            # Remove the most recently used key
            mru_key = self.order.pop()  # Remove the last item
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

        # If key already exists, remove it to re-insert at the end
        if key in self.order:
            self.order.remove(key)

        # Add the new key-value pair
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache by key.
        Move the accessed item to the end to mark it as recently used.
        Return None if key is not found.
        """
        if key in self.cache_data:
            # Move the accessed key to the end to mark it as recently used
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None

    def print_cache(self):
        """Print the current cache state"""
        print("Current cache:")
        for key in self.order:
            print(f"{key}: {self.cache_data[key]}")
