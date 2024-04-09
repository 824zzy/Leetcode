""" https://leetcode.com/problems/maximum-subarray/
https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm

Or use bottom up dp template:
1. dp[0] = nums[0]
2. dp[i] = max(nums[i]+dp[i-1], nums[i])
"""
from header import *

# original kadane's algorithm


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans, cur = -inf, 0
        for x in nums:
            cur = max(x, cur + x)
            ans = max(ans, cur)
        return ans

# bottom-up dp kadane's algorithm


class Solution:
    def maxSubArray(self, A: List[int]) -> int:
        dp = [0] * len(A)
        dp[0] = A[0]
        for i in range(1, len(A)):
            dp[i] = max(dp[i - 1] + A[i], A[i])
        return max(dp)


# top-down dp kadane's algorithm
class Solution:
    def maxSubArray(self, A: List[int]) -> int:
        @cache
        def dp(i):
            if i == len(A):
                return 0
            return max(dp(i + 1) + A[i], A[i])

        return max(dp(i) for i in range(len(A)))
