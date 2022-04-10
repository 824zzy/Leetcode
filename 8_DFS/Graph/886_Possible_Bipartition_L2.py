""" https://leetcode.com/problems/possible-bipartition/
the same as 785, 
classical bipartite problem:
1. traverse the graph by bfs
2. check if any node has painted the same color
"""
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        G = defaultdict(list)
        for i, j in dislikes:
            G[i].append(j)
            G[j].append(i)
        
        seen = {}
        def dfs(i, color):
            if i in seen: return color*seen[i]>0
            seen[i] = color
            return all(dfs(j, -color) for j in G[i])
        
        return all(dfs(i, 1) for i in range(1, n+1) if i not in seen)