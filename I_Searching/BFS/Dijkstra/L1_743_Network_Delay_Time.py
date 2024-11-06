""" https://leetcode.com/problems/network-delay-time/
use dijkstra to find minimum delay for all the nodes to receive the signal
"""

from header import *


class Solution:
    def networkDelayTime(self, A: List[List[int]], n: int, k: int) -> int:
        G = [[] for _ in range(n + 1)]
        for i, j, w in A:
            G[i].append((j, w))

        pq = [(0, k)]
        dis = [inf] * (n + 1)
        dis[0] = dis[k] = 0
        while pq:
            d, i = heappop(pq)
            if d > dis[i]:
                continue
            for j, w in G[i]:
                new_d = d + w
                if new_d < dis[j]:
                    dis[j] = new_d
                    heappush(pq, (new_d, j))
        mx = max(dis)
        return mx if mx < inf else -1
