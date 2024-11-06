""" https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/
dijkstra template
"""

from header import *


class Solution:
    def minTimeToReach(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        Q = [[0, 0, 0]]
        dis = [[inf] * n for _ in range(m)]

        while Q:
            t, x, y = heappop(Q)
            if x == m - 1 and y == n - 1:
                return t
            if t > dis[x][y]:
                continue
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= x + dx < len(A) and 0 <= y + dy < len(A[0]):
                    tt = max(t, A[x + dx][y + dy]) + 1
                    if tt < dis[x + dx][y + dy]:
                        dis[x + dx][y + dy] = tt
                        heappush(Q, [tt, x + dx, y + dy])


"""
[0,4],
[4,4]
"""
