""" https://leetcode.com/problems/maximum-subarray/
https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm

Or use bottom up dp template:
1. dp[0] = nums[0]
2. dp[i] = max(nums[i]+dp[i-1], nums[i])
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans, cur = -inf, 0
        for x in nums:
            cur = max(0, cur) + x
            ans = max(ans, cur)
        return ans
