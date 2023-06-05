""" https://leetcode.com/problems/number-of-provinces/
use DSU to find clusters
"""
from header import *

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        dsu = {}
        def find(x):
            if x not in dsu: dsu[x] = x
            elif dsu[x]!=x: dsu[x] = find(dsu[x])
            return dsu[x]

        def union(x, y):
            dsu[find(x)] = find(y)
            
        
        for i, r in enumerate(isConnected):
            for j, x in enumerate(r):
                if x: union(i, j)
        return len(set(find(x) for x in dsu))