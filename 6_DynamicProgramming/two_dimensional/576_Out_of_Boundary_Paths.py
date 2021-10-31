""" L2: 3 dimensional DP
dp[i][j][k] means within k steps how many paths are available to reach boundary.
Note that k step will refer to k-1 step's status.
"""
class Solution:
    def findPaths(self, m, n, N, x, y):
        dp = [[[0 for _ in range(N+1)] for _ in range(n)] for _ in range(m)]
        for k in range(1, N+1):
            for i in range(m):
                for j in range(n):
                    v1 = i==0 or dp[i-1][j][k-1]
                    v2 = i==m-1 or dp[i+1][j][k-1]
                    v3 = j==0 or dp[i][j-1][k-1]
                    v4 = j==n-1 or dp[i][j+1][k-1]
                    dp[i][j][k] = (v1+v2+v3+v4)
        return dp[x][y][-1] % (10 ** 9 + 7)