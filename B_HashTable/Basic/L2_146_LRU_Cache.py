""" https://leetcode.com/problems/lru-cache/
use built-in dict which key is stored in the order of insertion
"""
from header import *

class LRUCache:
    def __init__(self, capacity: int):
        self.A = {}
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.A:
            val = self.A[key]
            self.A.pop(key)
            self.A[key] = va
            return val
        else:
            return -1
        
        
    def put(self, key: int, value: int) -> None:
        if key in self.A:
            self.A.pop(key)
        self.A[key] = value
        if len(self.A)>self.cap:
            self.A.pop(next(iter(self.A.keys())))