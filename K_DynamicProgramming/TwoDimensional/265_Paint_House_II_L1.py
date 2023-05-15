""" https://leetcode.com/problems/paint-house-ii/
"""
from header import *

class Solution:
    def minCostII(self, A: List[List[int]]) -> int:
        n = len(A)
        k = len(A[0])
        @cache
        def dp(i, pre):
            if i==len(A): 
                return 0
            c = inf
            for j in range(k):
                if pre!=j:
                    c = min(c, A[i][j]+dp(i+1, j))
            return c
            
        return dp(0, -1)
        
        
        
"""
[[11,20,4,3,19,3,18,17,6,8,18,18],
 [6,14,13,4,8,12,16,4,14,15,11,12],
 [8,1,4,20,19,9,12,11,13,12,1,3],
 [8,12,9,3,1,14,3,16,12,13,4,10],
 [17,1,1,5,17,10,20,15,3,9,18,3],
 [16,3,18,11,1,16,3,10,19,6,11,13]]
"""