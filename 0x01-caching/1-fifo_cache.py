#!/usr/bin/env python3
"""This main gee defines the FIFOCache class."""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache inherits from BaseCaching and
    implements a caching system using FIFO algorithm."""

    def __init__(self):
        """Initialize the FIFOCache."""
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache using FIFO algorithm.

        Args:
            key: The key for the item.
            item: The item to be cached.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Discard the first item put in cache (FIFO)
                discarded_key = next(iter(self.cache_data))
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)
            self.cache_data[key] = item

    def get(self, key):
        """Get an item from the cache.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The cached item if found, otherwise None.
        """
        if key is not None:
            return self.cache_data.get(key)
        return None