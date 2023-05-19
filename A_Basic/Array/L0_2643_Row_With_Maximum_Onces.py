""" https://leetcode.com/problems/row-with-maximum-ones/
linear scan
"""
from header import *
class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        mx, idx = 0, 0
        for i, x in enumerate(mat):
            sm = sum(x)
            if sm>mx:
                mx = sm
                idx = i
        return [idx, mx]