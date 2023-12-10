""" https://leetcode.com/problems/minimum-number-of-coins-for-fruits/
knap-sack dp
"""
from header import *
class Solution:
    def minimumCoins(self, A: List[int]) -> int:
        @cache
        def dp(i):
            if i>len(A):
                return 0
            ans = inf
            for j in range(i+1, 2*i+2):
                ans = min(ans, dp(j))
            return ans+A[i-1]
        return dp(1)
            
        
"""
[3,1,2]
[1,10,1,1]
[26,18,6,12,49,7,45,45]
[27,17,29,45,3,39,42,26]
[14,37,37,38,24,15,12]
"""