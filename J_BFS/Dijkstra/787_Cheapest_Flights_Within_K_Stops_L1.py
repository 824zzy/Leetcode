""" https://leetcode.com/problems/cheapest-flights-within-k-stops/
use dijkstra, consider cost and k together as heuristics in heap and seen.
"""
from header import *

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        G = defaultdict(dict) 
        for i, j, c in flights:
            G[i][j] = c
            
        k += 1
        Q = [(0, src, k)]
        seen = {(0, src)}
        while Q:
            cost, i, k = heappop(Q)
            if i==dst: return cost
            for j in G[i]:
                if (j, cost+G[i][j]) not in seen and k:
                    seen.add((j, cost+G[i][j]))
                    heappush(Q, (cost+G[i][j], j, k-1))
        return -1