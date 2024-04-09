""" https://leetcode.com/problems/path-with-minimum-effort/discuss/1035940/Python-dfs-with-binary-search-explained
A comprehensive problem for binary search and dfs/bfs
Similar problem: 778. Swim in Rising Water
"""
from header import *


class Solution:
    def minimumEffortPath(self, G: List[List[int]]) -> int:
        def fn(m):  # bfs
            Q = [(0, 0)]
            seen = {(0, 0)}
            while Q:
                x, y = Q.pop(0)
                if x == len(G) - 1 and y == len(G[0]) - 1:
                    return True
                for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    if 0 <= x + dx < len(G) and 0 <= y + dy < len(G[0]):
                        if abs(G[x + dx][y + dy] - G[x][y]
                               ) <= m and (x + dx, y + dy) not in seen:
                            seen.add((x + dx, y + dy))
                            Q.append((x + dx, y + dy))
            return False

        def fn(m):  # dfs
            seen = {(0, 0)}

            def dfs(x, y):
                if x == len(G) - 1 and y == len(G[0]) - 1:
                    return True
                ans = False
                for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    if 0 <= x + dx < len(G) and 0 <= y + dy < len(G[0]):
                        if abs(G[x + dx][y + dy] - G[x][y]
                               ) <= m and (x + dx, y + dy) not in seen:
                            seen.add((x + dx, y + dy))
                            ans |= dfs(x + dx, y + dy)
                return ans
            return dfs(0, 0)

        l, r = 0, max(max(G, key=max))
        while l < r:
            m = (l + r) // 2
            if fn(m):
                r = m
            else:
                l = m + 1
        return l
