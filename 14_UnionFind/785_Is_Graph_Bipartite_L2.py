""" https://leetcode.com/problems/is-graph-bipartite/
Intuition: if i and j belong to the same group, the graph is not bipartite

use disjoint set to union all the neighbors of every node
"""
class DSU:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        if self.p[x]!=x: self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)
        
        
class Solution:
    def isBipartite(self, A: List[List[int]]) -> bool:
        dsu = DSU(len(A))
        for i, nodes in enumerate(A):
            ii = dsu.find(i)
            for j in nodes:
                jj = dsu.find(j)
                # if i and j belong to the same group, the graph is not bipartite
                if ii==jj: return False
                dsu.union(nodes[0], j)
        return True
    
"""
[[1],[0],[4],[4],[2,3]]
[[4],[],[4],[4],[0,2,3]]
[[1,2,3],[0,2],[0,1,3],[0,2]]
[[1,3],[0,2],[1,3],[0,2]]
"""