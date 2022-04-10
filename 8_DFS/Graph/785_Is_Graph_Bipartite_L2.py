""" https://leetcode.com/problems/is-graph-bipartite/
the same as 886, 
classical bipartite problem:
1. traverse the graph by bfs
2. check if any node has painted the same color
"""
class Solution:
    def isBipartite(self, G: List[List[int]]) -> bool:
        seen = {}
        
        def dfs(i, color):
            if i in seen: return seen[i]*color>0
            seen[i] = color
            return all(dfs(j, -color) for j in G[i])
        
        return all(dfs(i, 1) for i in range(len(G)) if i not in seen)