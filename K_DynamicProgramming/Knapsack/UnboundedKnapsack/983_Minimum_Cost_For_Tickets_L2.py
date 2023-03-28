""" https://leetcode.com/problems/minimum-cost-for-tickets/
dp + binary search
1. use unbounded knapsack to find the minimum cost
2. use binary search or two conditions when d>=A[i] and d<A[i] to find next day for traveling
"""
from header import *

class Solution:
    def mincostTickets(self, A: List[int], costs: List[int]) -> int:
        @cache
        def dp(i):
            if i>=len(A): return 0
            ans = inf
            for d, c in zip(costs, (1, 7, 30)):
                j = bisect_right(A, A[i]+d-1)
                ans = min(ans, c+dp(j))
            return ans
        
        return dp(0)
    

class Solution:
    def mincostTickets(self, A: List[int], costs: List[int]) -> int:
        @cache
        def dp(i, d):
            if i==len(A) or d>=A[-1]: return 0
            if d>=A[i]: return dp(i+1, d)
            if d<A[i]: d = A[i]
            ans = inf
            for c, p in zip(costs, (1, 7, 30)):
                ans = min(ans, c+dp(i+1, d+p-1))
            return ans
        return dp(0, 0)