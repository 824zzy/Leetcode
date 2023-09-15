""" https://leetcode.com/problems/min-cost-to-connect-all-points/
Prim's algorithm template

Time: O(ElogV)=O(N^2*logN) due to the graph creation
"""
from header import *

class Solution:
    def minCostConnectPoints(self, A: List[List[int]]) -> int:
        G = defaultdict(dict)
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                dist = abs(A[i][0]-A[j][0])+abs(A[i][1]-A[j][1])
                G[i][j] = dist
                G[j][i] = dist
        
        seen = set()
        minHeap = [[0, 0]]  # pair of (dist, vertex)
        total_dist = 0
        while len(seen)<len(A):
            dist, u = heappop(minHeap)
            if u in seen: continue
            seen.add(u)
            total_dist += dist
            for v, d in G[u].items():
                if v not in seen:
                    heappush(minHeap, [d, v])
        return total_dist