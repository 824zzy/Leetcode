""" https://leetcode.com/problems/rearrange-array-elements-by-sign/
"""
from header import *

class Solution:
    def rearrangeArray(self, A: List[int]) -> List[int]:
        ans, pos, neg = [], [], []
        for x in A:
            if x>0: pos.append(x)
            else: neg.append(x)
        for x, y in zip(pos, neg):
            ans.extend([x, y])
        return ans