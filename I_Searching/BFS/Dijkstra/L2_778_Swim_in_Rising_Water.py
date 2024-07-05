""" https://leetcode.com/problems/swim-in-rising-water/
use max(depth, previous_depth) as heuristic for dijkstra
"""


class Solution:
    def swimInWater(self, A: List[List[int]]) -> int:
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        pq = [(A[0][0], (0, 0))]
        N = len(A)
        seen = set()
        while pq:
            cost, (x, y) = heappop(pq)
            if x == N - 1 and y == N - 1:
                return cost
            if (x, y) not in seen:
                seen.add((x, y))
                for dx, dy in D:
                    if 0 <= x + dx < N and 0 <= y + dy < N:
                        heappush(pq, (max(A[x + dx][y + dy], cost), (x + dx, y + dy)))
