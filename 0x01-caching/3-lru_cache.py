#!/usr/bin/env python3
"""This function defines the LRUCache class."""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """The LRUCache inherits from BaseCaching an
    d is a caching system with LRU eviction."""

    def __init__(self):
        """Thus Initialize the LRUCache."""
        super().__init__()
        self.recently_used = []

    def put(self, key, item):
        """Thus Add an item to the cache.

        Args:
            key: This is the key for the item.
            item: The item to be cached.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.recently_used.remove(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = self.recently_used.pop(0)
                del self.cache_data[lru_key]
                print("DISCARD:", lru_key)
            self.cache_data[key] = item

        self.recently_used.append(key)

    def get(self, key):
        """Get an item from the cache.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The cached item if found, otherwise None.
        """
        if key is None or key not in self.cache_data:
            return None

        self.recently_used.remove(key)
        self.recently_used.append(key)
        return self.cache_data.get(key)