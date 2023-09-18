""" https://leetcode.com/problems/shortest-path-visiting-all-nodes/
1. floyd-warshall to find distances among all nodes
2. bit-mask top-down dp to find shortest path
"""
from header import *

class Solution:
    def shortestPathLength(self, G: List[List[int]]) -> int:
        N = len(G)
        # floyd-warshall
        dist = [[inf]*N for _ in range(N)]
        for i, x in enumerate(G):
            dist[i][i] = 0
            for j in x: dist[i][j] = 1
                
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
        
        @cache
        def dp(i, mask):
            if mask==0: return 0
            ans = inf
            for j in range(N):
                if mask & (1<<j):
                    ans = min(ans, dist[i][j]+dp(j, mask ^ (1<<j)))
            return ans
            
        return min(dp(i, (1<<N)-1) for i in range(N))