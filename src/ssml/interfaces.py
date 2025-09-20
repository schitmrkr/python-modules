# src/ssml/interfaces.py
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Union, Dict


# --- Node definitions ---
SSMLNode = Union["SSMLText", "SSMLTag"]


@dataclass
class SSMLTag:
    name: str
    attributes: Dict[str, str]
    children: List[SSMLNode]


@dataclass
class SSMLText:
    text: str


# --- Interface for the parser ---
class SSMLParser(ABC):
    """Interface for an SSML parser."""

    @abstractmethod
    def parse(self, ssml: str) -> SSMLNode:
        """Parse an SSML string into a tree of SSMLTag/SSMLText nodes."""
        pass

    @abstractmethod
    def to_text(self, node: SSMLNode) -> str:
        """Extract plain text content from an SSML node tree."""
        pass

    @abstractmethod
    def escape(self, text: str) -> str:
        """Escape special XML characters (<, >, &) in text."""
        pass

    @abstractmethod
    def unescape(self, text: str) -> str:
        """Unescape XML entities (&lt;, &gt;, &amp;) back to characters."""
        pass
