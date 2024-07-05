""" https://leetcode.com/problems/maximum-product-subarray/
We need to keep track of maximum and minimum product(product subarray) at the same time to make sure we can find global maximum.
"""
from header import *


class Solution:
    def maxProduct(self, A: List[int]) -> int:
        ans, maxP, minP = -inf, 1, 1

        for x in A:
            maxP, minP = max(x, maxP * x, minP * x), min(x, maxP * x, minP * x)
            ans = max(ans, maxP)
        return ans


# bottom up do
class Solution:
    def maxProduct(self, A: List[int]) -> int:
        dp = [[1, 1] for _ in range(len(A))]
        dp[0] = (A[0], A[0])
        for i in range(1, len(A)):
            dp[i][0] = max(A[i], dp[i - 1][0] * A[i], dp[i - 1][1] * A[i])
            dp[i][1] = min(A[i], dp[i - 1][0] * A[i], dp[i - 1][1] * A[i])

        return max([dp[i][0] for i in range(len(A))])


# top down dp


class Solution:
    def maxProduct(self, A: List[int]) -> int:
        @cache
        def dp(i):
            if i == len(A):
                return 1, 1
            ma = max(A[i], A[i] * dp(i + 1)[0], A[i] * dp(i + 1)[1])
            mi = min(A[i], A[i] * dp(i + 1)[0], A[i] * dp(i + 1)[1])
            return ma, mi

        return max([dp(i)[0] for i in range(len(A))])
