""" https://leetcode.com/problems/lru-cache/
use OrderedDict
"""
from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
        return self.cache.get(key, -1)
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache)>self.cap:
            self.cache.popitem(last=False)