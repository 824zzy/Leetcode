""" https://leetcode.com/problems/minimum-cost-for-tickets/

"""
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        @lru_cache(None)
        def fn(i):
            """Return minimum cost of traveling on days[i:]"""
            if i == len(days): return 0 # boundary condition (no more travel)
            ans = inf
            for cost, d in zip(costs, (1, 7, 30)): 
                ii = bisect_left(days, days[i]+d)
                ans = min(ans, cost + fn(ii))
            return ans 
        
        return fn(0)