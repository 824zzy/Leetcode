""" https://leetcode.com/problems/minimum-cost-to-make-array-equal/
1. consider cost[i] as the frequency of nums[i]
2. when sum(cost) larger than total//2, then we find the median
"""
from header import *
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        nums, cost = zip(*sorted(zip(nums, cost)))
        total = sum(cost)
        prefix = 0 
        for i, x in enumerate(cost): 
            prefix += x
            if prefix > total//2: break 
        return sum(c*abs(x-nums[i]) for x, c in zip(nums, cost))