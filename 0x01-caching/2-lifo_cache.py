#!/usr/bin/env python3
"""
LIFOCache module
This module provides a caching system with LIFO eviction policy.
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache defines a caching system with LIFO eviction policy."""

    def __init__(self):
        """Initialize the LIFOCache with a LIFO eviction policy."""
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """Add an item to the cache with LIFO eviction if needed.

        If the cache exceeds MAX_ITEMS, remove the last added item.
        Args:
            key (str): The key under which to store the item.
            item (any): The item to store in the cache.
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        if key != self.last_key:
            self.last_key = key

        # check if we need to evict an item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # LIFO eviction: remove the last added item
            if self.last_key:
                del self.cache_data[self.last_key]
                print("DISCARD:", self.last_key)

            # Reset last_key to the previous entry if it exists
            if self.cache_data:
                self.last_key = list(self.cache_data.keys())[-1]

    def get(self, key):
        """Retrieve an item from the cache by key.

        Args:
            key (str): The key for the item to retrieve.

        Returns:
            any: The item associated with the key,
            or None if the key does not exist.
        """
        return self.cache_data.get(key, None)
