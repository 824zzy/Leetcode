""" https://leetcode.com/problems/min-cost-to-connect-all-points/
Kruskal's algorithm template

Time: O(ElogV)=O(N^2*logN) due to the graph creation
"""
from header import *

class DSU:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        if self.p[x]!=x: self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)
        
        
class Solution:
    def minCostConnectPoints(self, A: List[List[int]]) -> int:
        edges = []
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                dist = abs(A[i][0]-A[j][0])+abs(A[i][1]-A[j][1])
                edges.append((dist, i, j))
        edges.sort()
        
        ans = 0
        dsu = DSU(len(A))
        
        for cost, i, j in edges:
            if dsu.find(i)!=dsu.find(j):
                dsu.union(i, j)
                ans += cost
        return ans