""" https://leetcode.com/problems/maximum-profit-in-job-scheduling/description/
Since the data size is 5 * 10^4, the algorithm has to be O(nlogn) or O(n)
1. clearly, the algorithm has to be knapsack algorithm
2. the hard part is to come up with the idea of use binary search to find the next job index
"""
from header import *

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        A = sorted([(x, y, z) for x, y, z in zip(startTime, endTime, profit)])
        
        @cache
        def dp(i):
            if i==len(A): return 0
            # skip current job
            ans = dp(i+1)
            # choose current job, use binary search to find the next
            ii = bisect_left(A, (A[i][1], -inf, -inf))
            ans = max(ans, A[i][2]+dp(ii))
            return ans
        
        return dp(0)