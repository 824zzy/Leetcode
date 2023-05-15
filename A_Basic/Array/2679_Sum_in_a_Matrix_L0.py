""" https://leetcode.com/problems/sum-in-a-matrix/
simulation
"""
from header import *

class Solution:
    def matrixSum(self, A: List[List[int]]) -> int:
        A = [sorted(a) for a in A]
        ans = 0
        for c in zip(*A):
            ans += max(c)
        return ans