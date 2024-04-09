""" https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/description/
dijkstra along with the sorted queries
"""
from header import *


class Solution:
    def maxPoints(self, G: List[List[int]], queries: List[int]) -> List[int]:
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queries = sorted([(x, i) for i, x in enumerate(queries)])
        Q = [(G[0][0], 0, 0)]
        ans = [0] * len(queries)
        seen = {(0, 0)}
        cnt = 0

        for thres, i in queries:
            while Q and Q[0][0] < thres:
                _, x, y = heappop(Q)
                cnt += 1
                for dx, dy in D:
                    if 0 <= x + \
                            dx < len(G) and 0 <= y + dy < len(G[0]) and (x + dx, y + dy) not in seen:
                        seen.add((x + dx, y + dy))
                        heappush(Q, (G[x + dx][y + dy], x + dx, y + dy))
            ans[i] = cnt
        return ans
