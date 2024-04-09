""" https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
find the longest path in the graph by dfs
"""


class Solution:
    def longestIncreasingPath(self, A: List[List[int]]) -> int:
        neibs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        M, N = len(A), len(A[0])
        dp = [[0 for _ in range(N)] for _ in range(M)]
        ans = 0

        def dfs(x, y):
            if dp[x][y]:
                return dp[x][y]
            mx = 1
            for dx, dy in neibs:
                if 0 <= x + dx < M and 0 <= y + \
                        dy < N and A[x + dx][y + dy] > A[x][y]:
                    mx = max(mx, 1 + dfs(x + dx, y + dy))
            dp[x][y] = mx
            return mx

        for i in range(M):
            for j in range(N):
                ans = max(ans, dfs(i, j))
        return ans
