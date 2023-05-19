""" https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/
"""
from header import *

class Solution:
    def differenceOfSum(self, A: List[int]) -> int:
        a = sum(A)
        b = 0
        for x in A:
            for c in str(x):
                b += int(c)
        return abs(a-b)