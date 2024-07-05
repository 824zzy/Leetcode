""" https://leetcode.com/problems/number-of-islands/submissions/
count island by bfs
"""
from header import *


class Solution:
    def numIslands(self, A: List[List[str]]) -> int:
        m, n = len(A), len(A[0])
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(x, y):
            Q = [(x, y)]
            A[x][y] = "0"
            while Q:
                x, y = Q.pop(0)
                for dx, dy in D:
                    if 0 <= x + dx < m and 0 <= y + dy < n and A[x + dx][y + dy] == "1":
                        A[x + dx][y + dy] = "0"
                        Q.append((x + dx, y + dy))

        ans = 0
        for i in range(m):
            for j in range(n):
                if A[i][j] == "1":
                    bfs(i, j)
                    ans += 1
        return ans


""" https://leetcode.com/problems/number-of-islands/submissions/
count island by dfs
"""


class Solution:
    def numIslands(self, A: List[List[str]]) -> int:
        M, N = len(A), len(A[0])
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ans = 0

        def dfs(x, y):
            A[x][y] = "0"
            for dx, dy in D:
                if 0 <= x + dx < M and 0 <= y + dy < N and A[x + dx][y + dy] == "1":
                    dfs(x + dx, y + dy)

        for i in range(M):
            for j in range(N):
                if A[i][j] == "1":
                    ans += 1
                    dfs(i, j)
        return ans
