""" https://leetcode.com/problems/minimum-cost-for-tickets/
dp + binary search
use unbounded knapsack as dp and binary search to find next day for travelling
"""
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