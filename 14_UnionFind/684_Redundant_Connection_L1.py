""" https://leetcode.com/problems/redundant-connection/
if x and y belong to same set, return the redundant edge [x, y]
else union x and y to same set.
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
    def findRedundantConnection(self, A: List[List[int]]) -> List[int]:
        dsu = DSU(len(A)+1)
        for i, j in A:
            if dsu.find(i)==dsu.find(j): return [i, j]
            else: dsu.union(i, j)