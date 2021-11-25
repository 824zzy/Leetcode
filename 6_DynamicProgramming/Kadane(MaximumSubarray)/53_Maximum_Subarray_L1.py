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
    
# bottom up dp template
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i]+dp[i-1])
        return max(dp)