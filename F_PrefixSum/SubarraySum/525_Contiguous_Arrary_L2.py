""" https://leetcode.com/problems/contiguous-array/
1. compute prefix sum following the rule: 0==>-1, 1==>1
2. use seen to record the first occurrence of prefix
3. if a prefix sum has appeared before, it indicates that a piece of subarray sums to 0.
"""
from header import *

class Solution:
    def findMaxLength(self, A: List[int]) -> int:
        seen = {0: -1}
        ans = 0
        prefix = 0
        for i, x in enumerate(A):
            if x==0: prefix -= 1
            elif x==1: prefix += 1
            ans = max(ans, i - seen.setdefault(prefix, i))
        return ans