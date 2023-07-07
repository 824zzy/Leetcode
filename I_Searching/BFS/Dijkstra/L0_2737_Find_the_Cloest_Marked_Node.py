""" https://leetcode.com/problems/find-the-closest-marked-node/
directly apply Dijkstra's algorithm
"""
from header import *

class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], src: int, marked: List[int]) -> int:
        G = defaultdict(list)
        for u, v, w in edges: 
            G[u].append((v, w))

        pq = []
        heappush(pq, (0, src))
        seen = {}
        marked = set(marked)
        while pq:
            cost, i = heapq.heappop(pq)
            if i in marked:
                return cost
            if i not in seen:
                seen[i] = cost
                for j, w in G[i]:
                    heapq.heappush(pq, (cost+w, j))
        return -1