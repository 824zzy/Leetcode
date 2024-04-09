""" L1: https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/
bitmask template

TODO: how to write it in top down version???
"""
from functools import reduce


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [-1] * (1 << N)
        dp[0] = 0
        for mask in range(1 << N):
            for j in range(N):
                if mask & (1 << j):
                    neib = dp[mask ^ (1 << j)]
                    dp[mask] = neib | nums[j]
        return dp.count(max(dp))

# from ye15:
# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/discuss/1525225/Python3-top-down-dp


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        target = reduce(or_, nums)

        @cache
        def fn(i, mask):
            """Return number of subsets to get target."""
            if mask == target:
                return 2**(len(nums) - i)
            if i == len(nums):
                return 0
            return fn(i + 1, mask | nums[i]) + fn(i + 1, mask)

        return fn(0, 0)
