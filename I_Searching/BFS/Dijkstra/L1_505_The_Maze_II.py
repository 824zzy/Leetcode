""" https://leetcode.com/problems/the-maze-ii/
variant dijkstra algorithm to find the shortest path from start to end
"""
from header import *


class Solution:
    def shortestDistance(
        self, A: List[List[int]], start: List[int], destination: List[int]
    ) -> int:
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        Q = [(0, start[0], start[1])]
        m, n = len(A), len(A[0])
        seen = {(start[0], start[1]): 0}
        heapify(Q)

        while Q:
            d, x, y = heappop(Q)
            if [x, y] == destination:
                return d
            for dx, dy in D:
                _x, _y = x, y
                step = 0
                while (
                    0 <= _x + dx < m and 0 <= _y + dy < n and A[_x + dx][_y + dy] != 1
                ):
                    _x, _y = _x + dx, _y + dy
                    step += 1
                if (_x, _y) not in seen or d + step < seen[(_x, _y)]:
                    seen[_x, _y] = d + step
                    heappush(Q, (d + step, _x, _y))
        return -1
