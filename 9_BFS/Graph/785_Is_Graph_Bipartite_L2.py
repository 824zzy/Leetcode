""" https://leetcode.com/problems/is-graph-bipartite/
the same as 886,
classical bipartite problem:
1. traverse the graph by bfs
2. check if any node has painted the same color
"""
class Solution:
    def isBipartite(self, G: List[List[int]]) -> bool:
        seen = {}
        
        for i in range(len(G)):
            if i not in seen:
                Q = [(i, 1)]
                while Q:
                    i, color = Q.pop(0)
                    for j in G[i]:
                        if j not in seen:
                            seen[j] = -color
                            Q.append((j, -color))
                        elif seen[j]*color>0: return False
        return True