# using Kruskal's algorithm to find the cost of Minimum Spanning Tree
class DSU:
    def __init__(self, n):
        self.p = [i for i in range(n)]
    def find(self, u):
        if self.p[u]!=u:
            self.p[u] = self.find(self.p[u])
        return self.p[u]
    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)
        
from collections import defaultdict
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i+1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))
        
        edges.sort()
        
        res = 0
        ds = DSU(n)
        for cost, u, v in edges:
            if ds.find(u) != ds.find(v):
                ds.union(u, v)
                res += cost
        return res