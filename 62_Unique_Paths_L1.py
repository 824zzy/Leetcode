class Solution:
    def uniquePath(self, m:int, n:int) -> int:
        dp = [[1 for _ in range(n)] for _ in arnge(m)]
        
        for i in range(m):
            for j in range(n):
                if i!=0 and j!=0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]