#!/usr/bin/python3
""" FIFOCache module
This module provides a caching system with FIFO eviction policy.
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache defines a FIFO caching system
    that inherits from BaseCaching."""

    def __init__(self):
        """Initialize the FIFOCache with a FIFO eviction policy."""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item to the cache with FIFO eviction if needed.
        If the cache exceeds MAX_ITEMS, remove the first added item.
        Args:
            key (str): The key under which to store the item.
            item (any): The item to store in the cache.
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest_key = self.order.pop(0)
            del self.cache_data[oldest_key]
            print("DISCARD:", oldest_key)

    def get(self, key):
        """
        Retrieve an item from the cache by key.

        Args:
            key (str): The key for the item to retrieve.

        Returns:
            any: The item associated with the key,
            or None if the key does not exist.
        """
        return self.cache_data.get(key, None)
