""" https://leetcode.com/problems/double-modular-exponentiation/
use pow which implements fast power algorithm
"""
from header import *

class Solution:
    def getGoodIndices(self, A: List[List[int]], t: int) -> List[int]:
        ans = []
        for i, (a, b, c, m) in enumerate(A):
            if pow(pow(a, b, 10), c, m) == t: 
                ans.append(i)
        return ans