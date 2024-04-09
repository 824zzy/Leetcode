""" https://leetcode.com/problems/longest-increasing-subsequence/
use bisect to maintain a increasing list.
O(NlogN)
"""
from header import *


class Solution:
    def lengthOfLIS(self, A: List[int]) -> int:
        vals = []
        for x in A:
            k = bisect_left(vals, x)
            if k == len(vals):
                vals.append(x)
            else:
                vals[k] = x
        return len(vals)
