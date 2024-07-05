""" https://leetcode.com/problems/minimum-cost-to-reach-city-with-discounts/
carefully design the seen and pq to handle the discount
"""
from header import *


class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        G = defaultdict(dict)
        for i, j, w in highways:
            G[i][j] = w
            G[j][i] = w

        pq = [(0, 0, discounts)]
        seen = defaultdict(int)
        seen[(0, discounts)] = 0
        while pq:
            c, i, d = heappop(pq)
            if i == n - 1:
                return c
            for j in G[i]:
                if (j, d) not in seen or c + G[i][j] < seen[(j, d)]:
                    seen[(j, d)] = c + G[i][j]
                    heappush(pq, (c + G[i][j], j, d))
                if d and (j, d - 1) not in seen or c + G[i][j] // 2 < seen[(j, d - 1)]:
                    seen[(j, d - 1)] = c + G[i][j] // 2
                    heappush(pq, (c + G[i][j] // 2, j, d - 1))
        return -1


"""
5
[[0,1,4],[2,1,3],[1,4,11],[3,2,3],[3,4,2]]
1
4
[[1,3,17],[1,2,7],[3,2,5],[0,1,6],[3,0,20]]
20
4
[[0,1,3],[2,3,2]]
0
5
[[0,1,0],[2,1,0],[1,4,11],[3,2,0],[3,4,0]]
4
6
[[0,1,2],[1,3,4],[0,2,6],[2,3,8],[3,4,100],[4,5,200]]
2
"""
