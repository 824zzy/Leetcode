""" https://leetcode.com/problems/minimum-cost-to-buy-apples/
simulation using dijkstra template
"""
from header import *


class Solution:
    def minCost(
        self, n: int, roads: List[List[int]], A: List[int], k: int
    ) -> List[int]:
        G = defaultdict(dict)
        for i, j, w in roads:
            G[i][j] = w
            G[j][i] = w
        ans = []
        for i in range(1, n + 1):
            seen = {i: 0}
            Q = [(0, i)]
            mn = A[i - 1]
            while Q:
                c, x = heappop(Q)
                for y, cc in G[x].items():
                    nxt_c = c + cc * (k + 1)
                    if y not in seen or nxt_c < seen[y]:
                        mn = min(mn, A[y - 1] + c + cc * (k + 1))
                        seen[y] = nxt_c
                        heappush(Q, (nxt_c, y))
            ans.append(mn)
        return ans
