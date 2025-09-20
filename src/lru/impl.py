# src/lru/impl.py
from typing import Any, Optional
from collections import OrderedDict
from .interfaces import LRUCache

class LRUCacheImpl(LRUCache):
    """Concrete implementation of an LRU cache using OrderedDict."""

    def __init__(self, item_limit: int):
        self.capacity = item_limit
        self.cache = OrderedDict()

    def has(self, key: str) -> bool:
        if key in self.cache:
            self.cache.move_to_end(key)
            return True
        return False

    def get(self, key: str) -> Optional[Any]:
        if key not in self.cache:
            return None
        self.cache.move_to_end(key)
        return self.cache[key]

    def set(self, key: str, value: Any) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
