# From end to start
class Solution:
    def calculateMinimumHP(self, d: List[List[int]]) -> int:
        m, n = len(d), len(d)
        dp = [[float('inf')]*(n+1)] * (m+1)
        # must have 1hp when arrived terminal point
        dp[m][n-1] = dp[m-1][n] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                # make sure knight won't dead by max(1, x)
                dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1])-dp[i][j])
        return dp[0][0]