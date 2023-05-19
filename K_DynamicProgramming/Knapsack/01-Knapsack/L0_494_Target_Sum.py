""" https://leetcode.com/problems/target-sum/
typical 01 Knapsack problem
"""
from header import *

class Solution:
    def findTargetSumWays(self, A: List[int], t: int) -> int:
        @cache
        def dp(i, sm):
            if i==len(A):
                return sm==t
            return dp(i+1, sm+A[i])+dp(i+1, sm-A[i])
        
        return dp(0, 0)