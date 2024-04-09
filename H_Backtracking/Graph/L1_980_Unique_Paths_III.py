""" https://leetcode.com/problems/unique-paths-iii/
implementation: use backtracking to find all valid paths
"""
from header import *


class Solution:
    def uniquePathsIII(self, A: List[List[int]]) -> int:
        M, N = len(A), len(A[0])
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        obs = 0
        for i in range(M):
            for j in range(N):
                if A[i][j] == -1:
                    obs += 1
                if A[i][j] == 1:
                    s = (i, j)

        def dfs(x, y, cnt):
            if A[x][y] == 2 and cnt == M * N - obs:
                return 1
            ans = 0
            tmp = A[x][y]
            A[x][y] = -1
            for dx, dy in D:
                if 0 <= x + dx < M and 0 <= y + \
                        dy < N and A[x + dx][y + dy] != -1:
                    ans += dfs(x + dx, y + dy, cnt + 1)
            A[x][y] = tmp
            return ans

        ans = dfs(s[0], s[1], 1)
        return ans
