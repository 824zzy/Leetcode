""" https://leetcode.com/problems/shortest-path-visiting-all-nodes/
1. floyd-warshall to find distances among all nodes
2. bit-mask top-down dp to find shortest path
"""
class Solution:
    def shortestPathLength(self, G: List[List[int]]) -> int:
        dist = [[inf]*len(G) for _ in range(len(G))]
        # floyd-warshall
        for i, x in enumerate(G):
            dist[i][i] = 0
            for j in x: dist[i][j] = 1
                
        for k in range(len(G)):
            for i in range(len(G)):
                for j in range(len(G)):
                    dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
        
        # bit mask
        @cache
        def dp(i, mask):
            if mask==0: return 0
            ans = inf
            for j in range(len(G)):
                if mask & (1<<j):
                    ans = min(ans, dist[i][j]+dp(j, mask ^ (1<<j)))
            return ans
            
        return min(dp(i, (1<<len(G))-1) for i in range(len(G)))