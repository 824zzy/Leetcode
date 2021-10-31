""" L1: Classical 2D DP
dp[i][j] = A[i][j] + min(dp[i-1][j], dp[i][j-1])
"""
class Solution:
    def minPathSum(self, A: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                if i==0 and j==0: dp[i][j] = A[0][0]
                elif i==0: dp[i][j] = A[i][j] + dp[i][j-1]
                elif j==0: dp[i][j] = A[i][j] + dp[i-1][j]
                else: dp[i][j] = A[i][j] + min(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]