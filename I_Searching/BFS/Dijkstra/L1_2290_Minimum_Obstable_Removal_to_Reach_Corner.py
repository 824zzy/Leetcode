""" https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/
easy understanding but not optimal solution, see solution by dp
"""


class Solution:
    def minimumObstacles(self, A: List[List[int]]) -> int:
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        pq = [(1 if A[0][0] == 1 else 0, 0, 0)]
        seen = set()

        while pq:
            cost, x, y = heapq.heappop(pq)
            if x == len(A) - 1 and y == len(A[0]) - 1:
                return cost
            if (x, y) not in seen:
                seen.add((x, y))
                for dx, dy in D:
                    if 0 <= x + dx < len(A) and 0 <= y + dy < len(A[0]):
                        if A[x + dx][y + dy]:
                            heapq.heappush(pq, (cost + 1, x + dx, y + dy))
                        else:
                            heapq.heappush(pq, (cost, x + dx, y + dy))
