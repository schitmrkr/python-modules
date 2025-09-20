# src/lru/interfaces.py
from abc import ABC, abstractmethod
from typing import Any, Optional

class LRUCache(ABC):
    """Interface for an LRU cache."""

    @abstractmethod
    def has(self, key: str) -> bool:
        """Check if the key exists in the cache (marking it as recently used)."""
        pass

    @abstractmethod
    def get(self, key: str) -> Optional[Any]:
        """Get the value for a key, or None if not found (marking it as recently used)."""
        pass

    @abstractmethod
    def set(self, key: str, value: Any) -> None:
        """Insert or update the value for a key."""
        pass
