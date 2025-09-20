# main.py
from src.lru.impl import LRUCacheImpl
from src.lru.interfaces import LRUCache

from src.ssml.interfaces import SSMLParser
from src.ssml.impl import SSMLParserImpl

def demo_lru(cache: LRUCache):
    cache.set("a", 1)
    cache.set("b", 2)
    print(cache.get("a"))  # 1
    cache.set("c", 3)      # "b" evicted if capacity=2
    print(cache.has("b"))  # False

def demo_ssml(parser: SSMLParser):
    escaped = parser.escape("<><>")
    print(escaped)
    unescaped = parser.unescape(escaped)
    print(unescaped)


if __name__ == "__main__":
    # my_cache = LRUCacheImpl(item_limit=2)
    # demo_lru(my_cache)
    
    ssml_parser = SSMLParserImpl()
    demo_ssml(ssml_parser)
    

