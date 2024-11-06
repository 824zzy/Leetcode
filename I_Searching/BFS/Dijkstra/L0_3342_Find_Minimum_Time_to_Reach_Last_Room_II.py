""" https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/
dijkstra template
"""

from header import *


class Solution:
    def minTimeToReach(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        Q = [[0, 0, 0, 1]]
        dis = [[inf] * n for _ in range(m)]

        while Q:
            t, x, y, f = heappop(Q)
            if x == m - 1 and y == n - 1:
                return t
            if t > dis[x][y]:
                continue
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= x + dx < len(A) and 0 <= y + dy < len(A[0]):
                    tt = max(t, A[x + dx][y + dy]) + f
                    if tt < dis[x + dx][y + dy]:
                        dis[x + dx][y + dy] = tt
                        ff = 2 if f == 1 else 1
                        heappush(Q, [tt, x + dx, y + dy, ff])


"""
[[0,4],[4,4]]
[[0,0,0,0],[0,0,0,0]]
[[0,1],[1,2]]
[[1,62,18],[57,41,93]]
"""
