"""
https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/
1. Each cell is visited only once.
2. If the next cell's time is higher than the current timestamp, we need to go back and forth n times to reach the next cell's time:
    d + (2*n + 1) >= G[x+dx][y+dy] ==> n >= (G[x+dx][y+dy] - d - 1) / 2
"""

from header import *


class Solution:
    def minimumTime(self, G: List[List[int]]) -> int:
        if G[0][1] > 1 and G[1][0] > 1:
            return -1
        m, n = len(G), len(G[0])
        pq = [(0, 0, 0)]
        dis = [[inf for _ in range(n)] for _ in range(m)]

        while pq:
            d, x, y = heappop(pq)
            if x == m - 1 and y == n - 1:
                return d
            if d > dis[x][y]:
                continue
            for dx, dy in (0, 1), (-1, 0), (1, 0), (0, -1):
                if 0 <= x + dx < m and 0 <= y + dy < n and dis[x + dx][y + dy] == inf:
                    if G[x + dx][y + dy] <= d + 1:
                        nxt_d = d + 1
                        dis[x + dx][y + dy] = nxt_d
                        heappush(pq, (nxt_d, x + dx, y + dy))
                    else:
                        dd = ceil((G[x + dx][y + dy] - d - 1) / 2)
                        nxt_d = d + (2 * dd + 1)
                        dis[x + dx][y + dy] = nxt_d
                        heappush(pq, (nxt_d, x + dx, y + dy))
