""" https://leetcode.com/problems/tree-diameter/
dfs + greedy
"""
from header import *

class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        G = defaultdict(list)
        for i, j in edges:
            G[i].append(j)
            G[j].append(i)
        
        self.res = 0
        def dfs(i, p):
            d1, d2 = 0, 0
            for j in G[i]:
                if j!=p:
                    _d = 1+dfs(j, i)
                    if _d>d1:
                        d2 = d1
                        d1 = _d
                    elif _d>d2:
                        d2 = _d
            self.res = max(self.res, d1+d2)
            return max(d1, d2)
                    
        dfs(0, None)
        return self.res