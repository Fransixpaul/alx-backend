#!/usr/bin/env python3
"""
BaseCaching module
This module provides a basic caching system with no item limit.
"""

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """BasicCache inherits from BaseCaching with no caching limit."""
    def put(self, key, item):
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        if key is not None:
            return None
        return self.cache_data.get(key)