""" https://leetcode.com/problems/maximum-length-of-repeated-subarray/
binary search + tuple sliding window
"""
from header import *


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        def fn(m):
            seenA = set()
            for i in range(m, len(A) + 1):
                seenA.add(tuple(A[i - m : i]))
            seenB = set()
            for i in range(m, len(B) + 1):
                seenB.add(tuple(B[i - m : i]))
            return len(seenA & seenB) == 0

        l, r = 1, len(A) + 1
        while l < r:
            m = (l + r) // 2
            if fn(m):
                r = m
            else:
                l = m + 1
        return l - 1
