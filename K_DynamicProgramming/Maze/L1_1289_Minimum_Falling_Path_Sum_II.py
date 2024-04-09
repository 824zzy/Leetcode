""" https://leetcode.com/problems/minimum-falling-path-sum-ii/
"""


class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        M, N = len(A), len(A[0])
        dp = [[0 for j in range(N)] for i in range(M)]
        for j in range(N):
            dp[0][j] = A[0][j]
        for i in range(1, M):
            for j in range(N):
                dp[i][j] = min(x for k, x in enumerate(
                    dp[i - 1]) if k != j) + A[i][j]
        return min(dp[-1])


class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        M, N = len(A), len(A[0])

        @cache
        def dfs(i, j):
            if i < 0:
                return 0
            return min([dfs(i - 1, jj) + A[i][jj]
                       for jj in range(N) if j != jj])

        return dfs(M - 1, inf)
