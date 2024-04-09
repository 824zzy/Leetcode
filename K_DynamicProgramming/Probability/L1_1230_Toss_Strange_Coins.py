""" https://leetcode.com/problems/toss-strange-coins/
"""
from header import *


class Solution:
    def probabilityOfHeads(self, A: List[float], t: int) -> float:
        @cache
        def dp(i, sm):
            if i == len(A):
                return sm == t
            # pruning
            if sm > t:
                return 0
            ans = A[i] * dp(i + 1, sm + 1)
            ans += (1 - A[i]) * dp(i + 1, sm)
            return ans
        return dp(0, 0)


class Solution:
    def probabilityOfHeads(self, A: List[float], t: int) -> float:
        n = len(A)
        dp = [[0 for _ in range(t + 2)] for _ in range(n + 1)]
        dp[-1][t] = 1
        for i in reversed(range(n)):
            for j in reversed(range(t + 1)):
                dp[i][j] = A[i] * dp[i + 1][j + 1]
                dp[i][j] += (1 - A[i]) * dp[i + 1][j]
        return dp[0][0]


"""
[0.4]
1
[0.5,0.5,0.5,0.5,0.5]
0
"""
