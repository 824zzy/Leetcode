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
            res = self.A.pop(key)
            self.A[key] = res
            return res
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.A:
            self.A.pop(key)
        elif self.c == len(self.A):
            # or: self.A.pop(list(self.A.keys())[0]) but slower
            self.A.pop(next(iter(self.A.keys())))
        self.A[key] = value
