""" https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/
dp(i, d) = min(max(A[i:j]) + dp(j, d-1)), j = i+1, ...
"""
from header import *


class Solution:
    def minDifficulty(self, A: List[int], d: int) -> int:
        @cache
        def dp(i, d):
            if d == 1:
                return max(A[i:])

            ans = inf
            x = 0
            for j in range(i, len(A) - d + 1):
                x = max(x, A[j])
                ans = min(ans, x + dp(j + 1, d - 1))
            return ans

        return dp(0, d)


class Solution:
    def minDifficulty(self, A: List[int], d: int) -> int:
        n, inf = len(A), float('inf')
        dp = [[inf] * n + [0] for i in range(d + 1)]
        for d in range(1, d + 1):
            for i in range(n - d + 1):
                maxd = 0
                for j in range(i, n - d + 1):
                    maxd = max(maxd, A[j])
                    dp[d][i] = min(dp[d][i], maxd + dp[d - 1][j + 1])
        return dp[d][0] if dp[d][0] < inf else -1
