""" https://leetcode.com/problems/lru-cache/
use OrderedDict / Built-in dict
"""
from header import *

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


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.A = {}
        
    def get(self, key: int) -> int:
        if key not in self.A: return -1
        ans = self.A.pop(key)
        self.A[key] = ans
        return ans
        
        
    def put(self, key: int, value: int) -> None:
        if key in self.A: self.A.pop(key)
        self.A[key] = value
        if len(self.A)>self.cap:
            self.A.pop(next(iter(self.A.keys())))