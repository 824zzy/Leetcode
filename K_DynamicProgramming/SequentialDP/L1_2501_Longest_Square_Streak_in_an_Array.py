""" https://leetcode.com/problems/longest-square-streak-in-an-array/description/
dp[x] = dp[isqrt(x)] + 1
"""
from header import *

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        nums.sort()
        for x in nums:
            dp[x] = 1
            if sqrt(x)==isqrt(x):
                dp[x] = dp[isqrt(x)] + 1
        return max(dp.values()) if max(dp.values())!=1 else -1