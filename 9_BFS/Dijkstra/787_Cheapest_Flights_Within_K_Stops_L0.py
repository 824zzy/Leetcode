""" https://leetcode.com/problems/cheapest-flights-within-k-stops/
use dijkstra, consider cost and k together as heuristics in heap and seen.
"""
class Solution:
    def findCheapestPrice(self, n: int, F: List[List[int]], src: int, dst: int, k: int) -> int:
        G = collections.defaultdict(dict)
        for i, j, w in F: G[i][j] = w
        
        pq = [(0, k, src)]
        seen = {}
        while pq:
            cost, k, i = heappop(pq)
            if i==dst: return cost
            if (i, k) not in seen:
                seen[(i, k)] = cost
                for j in G[i]:
                    if k>=0: heappush(pq, (cost+G[i][j], k-1, j))
        return -1