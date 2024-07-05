""" https://leetcode.com/problems/count-all-alternating-subarrays/
dependent dp, dp[i] refers to the number of alternating subarrays ending at i
"""
from header import *

# top down solution


class Solution:
    def countAlternatingSubarrays(self, A: List[int]) -> int:
        @cache
        def dp(i):
            res = 1
            if i and A[i - 1] != A[i]:
                res += dp(i - 1)
            return res

        return sum(dp(i) for i in range(len(A)))


# bottom up solution
class Solution:
    def countAlternatingSubarrays(self, A: List[int]) -> int:
        dp = [1] * len(A)
        for i in range(len(A)):
            if i and A[i - 1] != A[i]:
                dp[i] += dp[i - 1]
        return sum(dp)
