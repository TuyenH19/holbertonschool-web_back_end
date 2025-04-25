#!/usr/bin/env python3
"""
  Basic dictionary
"""
import sys
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic caching system with no limit"""

    def put(self, key, item):
        """Add an item to the cache"""
        if key is not None or item is not None:
            self.cache_data[key] = item
            return item


    def get(self, key):
        """Retrieve item from cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
