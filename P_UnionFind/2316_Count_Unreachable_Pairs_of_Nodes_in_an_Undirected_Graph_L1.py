""" https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/
1. find groups
2. count size of every group
3. count unreachable pairs
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
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        # find groups
        dsu = DSU(n)
        for x, y in edges: dsu.union(x, y)
        
        # count size of every group
        G = Counter([G[dsu.find(i)] for i in range(n)])
        V = list(G.values())
        sm = sum(V)
        
        # count unreachable pairs
        ans = 0
        for i in range(len(V)):
            sm -= V[i]
            ans += V[i]*sm
        return ans