""" https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/
use dijkstra to explore four directions' minimum costs
"""


class Solution:
    def minCost(self, A: List[List[int]]) -> int:
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        M, N = len(A), len(A[0])
        pq = [(0, (0, 0))]
        seen = set()
        while pq:
            cost, (i, j) = heapq.heappop(pq)
            if (i, j) == (M - 1, N - 1):
                return cost
            if (i, j) not in seen and 0 <= i < M and 0 <= j < N:
                seen.add((i, j))
                for dx, dy in D:
                    if (
                        (dx == 0 and dy == 1 and A[i][j] == 1)
                        or (dx == 0 and dy == -1 and A[i][j] == 2)
                        or (dx == 1 and dy == 0 and A[i][j] == 3)
                        or (dx == -1 and dy == 0 and A[i][j] == 4)
                    ):
                        heapq.heappush(pq, (cost, (i + dx, j + dy)))
                    else:
                        heapq.heappush(pq, (cost + 1, (i + dx, j + dy)))
