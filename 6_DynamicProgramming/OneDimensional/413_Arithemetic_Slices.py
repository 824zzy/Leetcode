""" L1: DP
dp[i] means how many arithemetic slices till nums[i]
"""
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for i in range(2, len(nums)):
            if nums[i]-nums[i-1]==nums[i-1]-nums[i-2]:
                dp[i] = dp[i-1]+1
        return sum(dp)