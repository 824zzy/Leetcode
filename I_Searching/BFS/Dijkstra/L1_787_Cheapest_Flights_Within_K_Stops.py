""" https://leetcode.com/problems/cheapest-flights-within-k-stops/
use dijkstra, consider cost and k together as heuristics in heap and seen.
"""
from header import *

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        G = defaultdict(dict)
        for i, j, w in flights:
            G[i][j] = w
        pq = [(0, src, -1)]
        seen = {src: (0, -1)}
        while pq:
            c, i, step = heappop(pq)
            if i==dst:
                return c
            if step+1>k: continue
            for j in G[i]:
                if j not in seen or c+G[i][j]<seen[j][0] or step+1<seen[j][1]:
                    seen[j] = (c+G[i][j], step+1)
                    heappush(pq, (c+G[i][j], j, step+1))
        return -1