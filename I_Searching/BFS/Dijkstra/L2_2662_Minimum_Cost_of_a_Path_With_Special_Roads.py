""" https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/
1. build graph
2. dijkstra
"""
from header import *


class Solution:
    def minimumCost(self,
                    s: List[int],
                    t: List[int],
                    A: List[List[int]]) -> int:
        G = defaultdict(lambda: defaultdict(lambda: inf))
        for i, j, x, y, c in A:
            G[(i, j)][(x, y)] = min(G[(i, j)][(x, y)], c)
            G[(s[0], s[1])][(i, j)] = min(G[(s[0], s[1])]
                                          [(i, j)], abs(s[0] - i) + abs(s[1] - j))
            G[(s[0], s[1])][(x, y)] = min(G[(s[0], s[1])]
                                          [(x, y)], abs(s[0] - x) + abs(s[1] - y))
            G[(i, j)][(t[0], t[1])] = min(
                G[(i, j)][(t[0], t[1])], abs(t[0] - i) + abs(t[1] - j))
            G[(x, y)][(t[0], t[1])] = min(
                G[(x, y)][(t[0], t[1])], abs(t[0] - x) + abs(t[1] - y))

        for idx_i in range(len(A)):
            for idx_j in range(len(A)):
                i, j, x, y, _ = A[idx_i]
                ii, jj, xx, yy, _ = A[idx_j]
                G[(x, y)][(ii, jj)] = min(
                    G[(x, y)][(ii, jj)], abs(x - ii) + abs(y - jj))

        pq = [(0, s[0], s[1])]
        seen = {}
        seen[(s[0], s[1])] = 0
        while pq:
            cost, x, y = heappop(pq)
            if x == t[0] and y == t[1]:
                return cost
            for (xx, yy), c in G[(x, y)].items():
                if (xx, yy) not in seen or cost + c < seen[(xx, yy)]:
                    seen[xx, yy] = cost + c
                    heappush(pq, (cost + c, xx, yy))


""" 5 7 10 8
[1,1]
[4,5]
[[1,2,3,3,2],[3,4,4,5,1]]
[3,2]
[5,7]
[[3,2,3,4,4],[3,3,5,5,5],[3,4,5,6,6]]
[1,1]
[10,8]
[[6,4,9,7,1],[5,2,2,1,3],[3,2,5,5,2]]
[1,1]
[4,6]
[[3,4,2,4,1],[2,5,4,2,5],[3,2,1,6,3]]
"""
