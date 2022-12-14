""" https://leetcode.com/problems/house-robber/
max(dp[i-1], A[i-1]+dp[i-2])
"""
from header import *

# top down
class Solution:
    def rob(self, A: List[int]) -> int:
        @cache
        def dp(i):
            if i>=len(A): return 0
            return max(dp(i+1), A[i]+dp(i+2))
        
        return dp(0)
    
# bottom up
class Solution:
    def rob(self, A: List[int]) -> int:
        dp = [0]*(len(A)+2)
        for i in reversed(range(len(A))):
            dp[i] = max(dp[i+1], A[i]+dp[i+2])
        return dp[0]