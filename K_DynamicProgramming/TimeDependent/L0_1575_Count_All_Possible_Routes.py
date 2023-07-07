""" https://leetcode.com/problems/count-all-possible-routes/
simple top down dp
"""
from header import *

class Solution:
    def countRoutes(self, A: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(A)
        MOD = 10**9+7
        
        @cache
        def dp(i, f):
            ans = 0
            if i==finish:
                ans += 1
            for j in range(n):
                if i!=j and abs(A[j]-A[i])<=f:
                    ans += dp(j, f-abs(A[j]-A[i]))
            return ans%MOD
        
        return dp(start, fuel)
    
"""
[2,3,6,8,4]
1
3
5
[4,3,1]
1
0
6
[5,2,1]
0
2
3
"""