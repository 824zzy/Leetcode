""" https://leetcode.com/problems/dungeon-game/
Search dp from end to start.
"""


class Solution:
    def calculateMinimumHP(self, A: List[List[int]]) -> int:
        M, N = len(A), len(A[0])

        @cache
        def dfs(i, j):
            if i == M or j == N:
                return inf
            if i == M - 1 and j == N - 1:
                return max(1, 1 - A[i][j])
            return max(1, min(dfs(i + 1, j), dfs(i, j + 1)) - A[i][j])

        return dfs(0, 0)


class Solution:
    def calculateMinimumHP(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        dp = [[float('inf') for _ in range(n + 1)] for _ in range(m + 1)]
        dp[m][n - 1] = dp[m - 1][n] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = max(1, min(dp[i + 1][j] - A[i]
                               [j], dp[i][j + 1] - A[i][j]))
        return dp[0][0]
