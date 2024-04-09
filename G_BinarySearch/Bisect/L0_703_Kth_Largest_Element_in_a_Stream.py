""" https://leetcode.com/problems/kth-largest-element-in-a-stream/
"""
from sortedcontainers import SortedList
from header import *


class KthLargest:
    def __init__(self, k: int, A: List[int]):
        self.A = sorted(A)
        self.k = k

    def add(self, v: int) -> int:
        bisect.insort(self.A, v)
        return self.A[-self.k]


# sorted container also works


class KthLargest:
    def __init__(self, k: int, A: List[int]):
        self.A = SortedList(A)
        self.k = k

    def add(self, val: int) -> int:
        self.A.add(val)
        return self.A[-self.k]
