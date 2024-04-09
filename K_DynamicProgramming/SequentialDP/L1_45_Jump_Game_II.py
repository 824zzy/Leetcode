""" https://leetcode.com/problems/jump-game-ii/
update maximum reach dp by: dp[i+j] = min(dp[i+j], dp[i]+1)

Time complexity: O(n*k), where n<=10^4, k<=10^3
"""
from header import *


class Solution:
    def jump(self, A: List[int]) -> int:
        dp = [float('inf')] * len(A)
        dp[0] = 0
        for i in range(len(A)):
            for j in range(1, A[i] + 1):
                if i + j < len(A):
                    dp[i + j] = min(dp[i + j], dp[i] + 1)
        return dp[-1]


class Solution:
    def jump(self, A: List[int]) -> int:
        @cache
        def dp(i):
            if i >= len(A) - 1:
                return 0
            ans = inf
            for j in range(i + 1, i + A[i] + 1):
                ans = min(ans, 1 + dp(j))
            return ans
        return dp(0)
