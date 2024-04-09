""" https://leetcode.com/problems/shortest-bridge/submissions/
1. dfs to paint two islands.
2. bfs to search the shortest path from one island to another.
"""
from header import *


class Solution:
    def shortestBridge(self, G: List[List[int]]) -> int:
        m, n = len(G), len(G[0])
        D = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        seen = set()

        def dfs(x, y):
            seen.add((x, y))
            for dx, dy in D:
                if 0 <= x + dx < m and 0 <= y + \
                        dy < n and G[x + dx][y + dy] == 1 and (x + dx, y + dy) not in seen:
                    dfs(dx + x, dy + y)

        i, j = next((i, j) for i in range(m) for j in range(n) if G[i][j])
        dfs(i, j)

        # solution 1: update Q in each iteration
        Q = list(seen)
        ans = 0
        while Q:
            nextQ = []
            for x, y in Q:
                for dx, dy in D:
                    if 0 <= x + dx < m and 0 <= y + \
                            dy < n and (x + dx, y + dy) not in seen:
                        if G[x + dx][y + dy] == 1:
                            return ans
                        nextQ.append((x + dx, y + dy))
                        seen.add((x + dx, y + dy))
            Q = nextQ
            ans += 1

        # solution 2: heap
        pq = [(0, x, y) for x, y in seen]
        while pq:
            cost, x, y = heappop(pq)
            for dx, dy in D:
                if 0 <= x + dx < m and 0 <= y + \
                        dy < n and (x + dx, y + dy) not in seen:
                    if G[x + dx][y + dy] == 1:
                        return cost
                    seen.add((x + dx, y + dy))
                    heappush(pq, (cost + 1, x + dx, y + dy))
