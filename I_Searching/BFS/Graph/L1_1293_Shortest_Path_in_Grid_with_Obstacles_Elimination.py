""" https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
bfs with state (k, x, y)
"""
from header import *


class Solution:
    def shortestPath(self, A: List[List[int]], k: int) -> int:
        Q = [(0, 0, 0, k)]
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        seen = {(k, 0, 0)}
        while Q:
            cost, x, y, k = heappop(Q)
            if x == len(A) - 1 and y == len(A[0]) - 1:
                return cost
            for dx, dy in D:
                if 0 <= x + dx < len(A) and 0 <= y + dy < len(A[0]):
                    if not A[x + dx][y +
                                     dy] and (k, x + dx, y + dy) not in seen:
                        seen.add((k, x + dx, y + dy))
                        heappush(Q, (cost + 1, x + dx, y + dy, k))
                    elif A[x + dx][y + dy] and k and (k - 1, x + dx, y + dy) not in seen:
                        seen.add((k - 1, x + dx, y + dy))
                        heappush(Q, (cost + 1, x + dx, y + dy, k - 1))
        return -1
