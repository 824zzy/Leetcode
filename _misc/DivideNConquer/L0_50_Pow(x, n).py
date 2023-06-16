""" https://leetcode.com/problems/powx-n/
"""
from header import *

class Solution:
    def myPow(self, a: float, b: int) -> float:
        @cache
        def dfs(x):
            if x==0:
                return 1
            if x==1:
                return a
            if x==-1:
                return 1/a
            if x&1:
                return dfs(x//2)*dfs(x//2+1)
            else:
                return dfs(x//2)*dfs(x//2)
        return dfs(b)
    
"""
2.00000
10
2.10000
3
2.00000
-2
0.44528
0
8.66731
4
"""