""" https://leetcode.com/problems/shortest-path-visiting-all-nodes/
bitmask + BFS/Dijkstra
"""
from header import *

# bitmask + Dijkstra


class Solution:
    def shortestPathLength(self, G: List[List[int]]) -> int:
        pq = [(0, i, 1 << i) for i in range(len(G))]
        heapify(pq)
        seen = set([(i, m) for _, i, m in pq])
        while pq:
            step, i, mask = heappop(pq)
            if mask == (1 << len(G)) - 1:
                return step
            for j in G[i]:
                if (j, mask | (1 << j)) not in seen:
                    seen.add((j, mask | (1 << j)))
                    heappush(pq, (step + 1, j, mask | (1 << j)))


# bitmask + BFS
class Solution:
    def shortestPathLength(self, G: List[List[int]]) -> int:
        Q = [(i, 1 << i) for i in range(len(G))]
        seen = set(Q)
        ans = 0
        while Q:
            newq = []
            for i, mask in Q:
                if mask == (1 << len(G)) - 1:
                    return ans
                for ii in G[i]:
                    if (ii, mask | (1 << ii)) not in seen:
                        newq.append((ii, mask | (1 << ii)))
                        seen.add((ii, mask | (1 << ii)))
            Q = newq
            ans += 1
