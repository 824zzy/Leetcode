""" https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/
dp(i, d) = min(max(A[i:j]) + dp(j, d-1)), j = i+1, ...
"""
from header import *

class Solution:
    def minDifficulty(self, A: List[int], d: int) -> int:
        @cache
        def dp(i, d):
            if d==1: return max(A[i:])
            
            ans = inf
            x = 0
            for j in range(i, len(A)-d+1):
                x = max(x, A[j])
                ans = min(ans, x+dp(j+1, d-1))
            return ans
        
        return dp(0, d)