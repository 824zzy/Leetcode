""" L3: 2D dp+dfs+bfs
dfs to find reachable nodes
bfs to find minimum cost
"""
class Solution:
    def minCost(self, A: List[List[int]]) -> int:
        n, m, k = len(A), len(A[0]), 0
        dp = [[float('inf')] * m for i in range(n)]
        dirt = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        bfs = []

        def dfs(x, y):
            if not (0 <= x < n and 0 <= y < m and dp[x][y]==float('inf')): return
            dp[x][y] = k
            bfs.append([x, y])
            dfs(x + dirt[A[x][y] - 1][0], y + dirt[A[x][y] - 1][1])
        dfs(0, 0)
        while bfs:
            k += 1
            bfs, bfs2 = [], bfs
            [dfs(x + i, y + j) for x, y in bfs2 for i, j in dirt]
        return dp[-1][-1]