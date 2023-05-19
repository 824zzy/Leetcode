""" https://leetcode.com/problems/increasing-triplet-subsequence/
Greedy, a special case in longest increasing subsequence
"""
from header import *

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i, j = float('inf'), float('inf')
        for k in nums:
            if i>=k:  i = k
            elif j>=k: j = k
            else: return True
        return False