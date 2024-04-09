""" https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/
3D time sequential DP
"""
from header import *


class Solution:
    def numberOfPaths(self, A: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        dp = [[[0] * k for _ in range(len(A[0]))] for _ in range(len(A))]
        dp[0][0][A[0][0] % k] += 1
        for i in range(1, len(A)):
            for kk in range(k):
                dp[i][0][(kk + A[i][0]) % k] += dp[i - 1][0][kk] % MOD

        for j in range(1, len(A[0])):
            for kk in range(k):
                dp[0][j][(kk + A[0][j]) % k] += dp[0][j - 1][kk] % MOD

        for i in range(1, len(A)):
            for j in range(1, len(A[0])):
                for kk in range(k):
                    dp[i][j][(kk + A[i][j]) % k] += (dp[i][j - 1]
                                                     [kk] + dp[i - 1][j][kk]) % MOD
        return dp[-1][-1][0] % MOD


# top down solution will TLE
class Solution:
    def numberOfPaths(self, A: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7

        @cache
        def dp(i, j, sm):
            if i == len(A) - 1 and j == len(A[0]) - 1:
                if sm % k == 0:
                    return 1
                else:
                    return 0

            ans = 0
            if i + 1 < len(A):
                ans += dp(i + 1, j, (sm + A[i + 1][j]) % k)
            if j + 1 < len(A[0]):
                ans += dp(i, j + 1, (sm + A[i][j + 1]) % k)
            return ans % MOD

        return dp(0, 0, A[0][0]) % MOD
