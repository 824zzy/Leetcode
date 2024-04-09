""" https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/
Extend Kadane's algo by keeping track of max and min of subarray sum respectively.
"""
from header import *

# button up


class Solution:
    def maxAbsoluteSum(self, A: List[int]) -> int:
        ans, maxS, minS = 0, 0, 0
        for x in A:
            maxS = max(0, maxS) + x
            minS = min(0, minS) + x
            ans = max(ans, maxS, -minS)
        return ans

# top down


class Solution:
    def maxAbsoluteSum(self, A: List[int]) -> int:
        @cache
        def dp(i):
            if i == len(A):
                return 0, 0
            mx, mn = dp(i + 1)
            return max(0, mx) + A[i], min(0, mn) + A[i]

        ans = 0
        for i in range(len(A)):
            mx, mn = dp(i)
            ans = max(ans, mx, -mn)
        return ans
