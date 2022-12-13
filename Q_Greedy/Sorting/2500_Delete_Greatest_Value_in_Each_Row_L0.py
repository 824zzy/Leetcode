""" https://leetcode.com/problems/delete-greatest-value-in-each-row/description/
1. sort the matrix
2. sum up max of each column
"""
from header import *

class Solution:
    def deleteGreatestValue(self, A: List[List[int]]) -> int:
        A = [sorted(x) for x in A]
        ans = 0
        for x in zip(*A):
            ans += max(x)
        return ans