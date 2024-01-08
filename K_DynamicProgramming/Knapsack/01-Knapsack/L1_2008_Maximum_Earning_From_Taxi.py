""" https://leetcode.com/problems/maximum-earnings-from-taxi/
the same as 1235
"""
from header import *

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        A = sorted(rides)
        
        @cache
        def dp(i):
            if i==len(A):
                return 0
            # skip
            ans = dp(i+1)
            # choose and find next use binary seach
            endtime = A[i][1]
            j = bisect_left(A, [endtime, 0, 0])
            ans = max(ans, A[i][1]-A[i][0]+A[i][2]+dp(j))
            return ans
            
        return dp(0)