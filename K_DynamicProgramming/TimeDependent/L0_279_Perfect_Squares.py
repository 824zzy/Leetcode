""" https://leetcode.com/problems/perfect-squares/submissions/
check all the perfect square from i+j*j<=n
and update by min(dp[i+j*j], dp[i] + 1);

Note that j**2 is slower than j*j.
"""
from header import *

class Solution:
    def numSquares(self, n: int) -> int:
        @cache
        def dp(n):
            if n==0: return 0
            ans = inf
            for x in reversed(range(1, int(sqrt(n))+1)):
                ans = min(ans, 1+dp(n-x*x))
            return ans
        
        return dp(n)
    
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [inf] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            for x in range(1, int(sqrt(i))+1):
                dp[i] = min(dp[i], 1+dp[i-x*x])
        return dp[-1]