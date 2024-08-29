""" https://leetcode.com/problems/count-sub-islands/
bfs template
"""

from header import *


class Solution:
    def countSubIslands(self, G1: List[List[int]], G2: List[List[int]]) -> int:
        def bfs(x, y):
            ans = True
            Q = [(x, y)]
            while Q:
                x, y = Q.pop(0)
                if G1[x][y] != 1:
                    ans = False
                for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                    if 0 <= x + dx < m and 0 <= y + dy < n and G2[x + dx][y + dy] == 1:
                        G2[x + dx][y + dy] = 0
                        Q.append((x + dx, y + dy))
            return ans

        m, n = len(G1), len(G1[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if G2[i][j] == 1:
                    ans += bfs(i, j)
        return ans
