""" https://leetcode.com/problems/reordered-power-of-2/
Think reversely, given all the power of 2, find the find the one which has the same digits as the input.
"""
from header import *

class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        A = [Counter(str(1<<i)) for i in range(30)]
        for c in A:
            if Counter(str(N))==c: return True
        return False