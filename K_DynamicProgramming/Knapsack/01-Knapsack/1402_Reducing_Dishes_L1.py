""" https://leetcode.com/problems/reducing-dishes/
1. sort the dishes
2. define the knapsack problem
    choose dish: (i+1-dis)*A[i]+dp(i+1, dis)
    discard dish: dp(i+1, dis+1)
"""
from header import *

class Solution:
    def maxSatisfaction(self, A: List[int]) -> int:
        A.sort()
        
        @cache
        def dp(i, dis):
            if i==len(A): return 0
            # choose
            c = (i+1-dis)*A[i]+dp(i+1, dis)
            # skip
            d = dp(i+1, dis+1)
            return max(c, d)
        
        return dp(0, 0)
