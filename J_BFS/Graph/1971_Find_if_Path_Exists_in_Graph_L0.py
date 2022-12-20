""" https://leetcode.com/problems/find-if-path-exists-in-graph/description/
use bfs to find if there is a path from source to destination
union find and dfs can also be used
"""
from header import *

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        G = defaultdict(list)
        for i, j in edges:
            G[i].append(j)
            G[j].append(i)
        
        Q = [source]
        seen = [0]*n
        seen[source] = 1
        while Q:
            i = Q.pop(0)
            if i==destination: return True
            for j in G[i]:
                if not seen[j]:
                    seen[j] = 1
                    Q.append(j)
        return False