""" https://leetcode.com/problems/h-index-ii/
"""
from header import *


class Solution:
    def hIndex(self, A: List[int]) -> int:
        l, r = 0, len(A)
        while l < r:
            m = (l + r) // 2
            if A[m] >= len(A) - m:
                r = m
            else:
                l = m + 1
        return len(A) - l


"""
[0,1,3,5,6]
[1,2,100]
[0]
[1]
"""
