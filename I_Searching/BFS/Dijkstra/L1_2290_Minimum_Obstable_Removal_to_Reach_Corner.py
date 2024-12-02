""" https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/
easy understanding but not optimal solution, see solution by dp
"""

from header import *


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        pq = [(0, 0, 0)]
        dis = [[inf] * n for _ in range(m)]

        while pq:
            d, x, y = heappop(pq)
            if x == m - 1 and y == n - 1:
                return d
            if d > dis[x][y]:
                continue
            for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                if 0 <= x + dx < m and 0 <= y + dy < n:
                    new_d = d + (grid[x + dx][y + dy] == 1)
                    if new_d < dis[x + dx][y + dy]:
                        dis[x + dx][y + dy] = new_d
                        heappush(pq, (new_d, x + dx, y + dy))
