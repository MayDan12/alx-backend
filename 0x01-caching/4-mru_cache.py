#!/usr/bin/env python3
"""This function defines the MRUCache class."""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """The MRUCache inherits from BaseCaching and
    implements a caching system using MRU algorithm."""

    def __init__(self):
        """Initialize the MRUCache."""
        super().__init__()
        self.most_recently_used = None

    def put(self, key, item):
        """Add an item to the cache using MRU algorithm.

        Args:
            key: The key for the item.
            item: The item to be cached.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if self.most_recently_used is not None:
                    print("DISCARD:", self.most_recently_used)
                    del self.cache_data[self.most_recently_used]
            self.cache_data[key] = item

        self.most_recently_used = key

    def get(self, key):
        """This Get an item from the cache.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The cached item if found, otherwise None.
        """
        if key is not None and key in self.cache_data:
            self.most_recently_used = key
            return self.cache_data[key]
        return None