#!/usr/bin/env python3
"""This function defines the LFUCache class."""

from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """The LFUCache inherits from BaseCaching and
    implements a caching system using LFU algorithm."""

    def __init__(self):
        """Initialize the LFUCache."""
        super().__init__()
        self.frequency = defaultdict(int)
        self.order = OrderedDict()

    def put(self, key, item):
        """Thus Add an item to the cache using LFU algorithm.

        Args:
            key: This is the key for the item.
            item: The item to be cached.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the existing item's value
            self.cache_data[key] = item
            # Increase the access frequency
            self.frequency[key] += 1
            # Move the item to the end to mark it as recently used
            self.order.move_to_end(key)
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Find the least frequently used items
                min_freq = min(self.frequency.values())
                least_freq_keys = [
                    k for k, v in self.frequency.items() if v == min_freq]

                # Use LRU strategy among the least frequently used items
                for k in self.order:
                    if k in least_freq_keys:
                        discard_key = k
                        break

                print("DISCARD:", discard_key)
                del self.cache_data[discard_key]
                del self.frequency[discard_key]
                del self.order[discard_key]

            # Add the new item to the cache
            self.cache_data[key] = item
            self.frequency[key] = 1
            self.order[key] = None

    def get(self, key):
        """Get an item from the cache.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The cached item if found, otherwise None.
        """
        if key is not None and key in self.cache_data:
            # Increase the access frequency
            self.frequency[key] += 1
            # Move the item to the end to mark it as recently used
            self.order.move_to_end(key)
            return self.cache_data[key]
        return None