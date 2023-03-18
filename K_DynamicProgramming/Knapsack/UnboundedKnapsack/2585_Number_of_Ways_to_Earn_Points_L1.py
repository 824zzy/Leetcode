""" https://leetcode.com/problems/number-of-ways-to-earn-points/
template problem

Time complexity: O(n*t*cnt) ~= 50*1000*50
"""
from header import *

class Solution:
    def waysToReachTarget(self, target: int, A: List[List[int]]) -> int:
        MOD = 10**9+7 
        
        @cache
        def dp(i, p):
            if p==target: return 1
            if i==len(A): return 0
            ans = 0
            for j in range(A[i][0]+1):
                if p+j*A[i][1]<=target:
                    ans += dp(i+1, p+j*A[i][1])%MOD
            return ans%MOD
        
        return dp(0, 0)