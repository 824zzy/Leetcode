""" L2
if x and y belong to same set, return the redundant edge [x, y]
else union x and y to same set.
"""
class DSU:
    def __init__(self, n):
        self.p = [i for i in range(n)]
    
    def find(self, u):
        if self.p[u]!=u:
            self.p[u] = self.find(self.p[u])
        return self.p[u]
    
    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges)+1)
        for x, y in edges:
            if dsu.find(x)==dsu.find(y): return [x, y]
            else: dsu.union(x, y)