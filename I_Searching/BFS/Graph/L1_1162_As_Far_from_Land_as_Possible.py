""" https://leetcode.com/problems/as-far-from-land-as-possible/
multi-source bfs
"""
from header import *


class Solution:
    def maxDistance(self, G: List[List[int]]) -> int:
        Q = [(i, j) for i in range(len(G)) for j in range(len(G)) if G[i][j] == 1]

        ans = -1
        while Q:
            for _ in range(len(Q)):
                x, y = Q.pop(0)
                for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    if (
                        0 <= x + dx < len(G)
                        and 0 <= y + dy < len(G)
                        and G[x + dx][y + dy] == 0
                    ):
                        G[x + dx][y + dy] = 1
                        Q.append((x + dx, y + dy))
            ans += 1
        return ans if ans else -1
