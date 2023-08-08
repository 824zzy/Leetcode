""" https://leetcode.com/problems/minimum-costs-using-the-train-line/
"""
from header import *

class Solution:
    def minimumCosts(self, R: List[int], E: List[int], c: int) -> List[int]:
        A = list(zip(R, E))
        dp = [[inf, inf] for i in range(len(R))]
        dp[-1][0] = 0
        dp[-1][1] = c
        for i in range(len(R)):
            for j in (0, 1):
                dp[i][j] = min(A[i][j]+dp[i-1][j], c*(j==1)+A[i][(j+1)%2]+dp[i-1][(j+1)%2])
        return [min(x) for x in dp]
    
    
    
class Solution:
    def minimumCosts(self, R: List[int], E: List[int], c: int) -> List[int]:
        A = list(zip(R, E))
        
        @cache
        def dp(i, j):
            if i==-1:
                return 0 if j==0 else c
            return min(A[i][j]+dp(i-1, j), c*(j==1)+A[i][(j+1)%2]+dp(i-1, (j+1)%2))
        
        return [dp(i, 0) for i in range(len(A))]