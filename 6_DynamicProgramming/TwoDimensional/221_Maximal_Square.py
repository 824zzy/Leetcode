"""L1: 2D DP
dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])+1
"""
class Solution:
    def maximalSquare(self, A: List[List[str]]) -> int:
        if not A or not A[0]: return 0
        dp = [[0 for j in range(len(A[0])+1)] for i in range(len(A)+1)]
        ma = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if i==0 or j==0: dp[i][j] = int(A[i][j])
                else:
                    if A[i][j]=='1':
                        dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])+1
                ma = max(ma, dp[i][j])
        return ma*ma