""" https://leetcode.com/problems/kth-largest-element-in-a-stream/
"""
from header import *

class KthLargest:
    def __init__(self, k: int, A: List[int]):
        self.A = A
        heapify(self.A)
        self.k = k

    def add(self, v: int) -> int:
        heappush(self.A, v)
        return nlargest(self.k, self.A)[-1]