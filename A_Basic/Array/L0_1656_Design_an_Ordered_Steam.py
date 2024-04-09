""" https://leetcode.com/problems/design-an-ordered-stream/
use a pointer to control which part of A to print out
"""
from header import *


class OrderedStream:
    def __init__(self, n: int):
        self.A = [None] * (n + 2)
        self.p = 1

    def insert(self, k: int, v: str) -> List[str]:
        self.A[k] = v
        ans = []
        while self.A[self.p] is not None:
            ans.append(self.A[self.p])
            self.p += 1
        return ans
