class Solution:
    def uniquePathsWithObstacles(self, A: List[List[int]]) -> int:
        if A[0][0]==1: return 0
        m, n = len(A), len(A[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
        for i in range(1, m):
            if dp[i-1][0]==1 and A[i][0]==0: dp[i][0] = 1
            else: dp[i][0] = 0
        for j in range(1, n):
            if dp[0][j-1]==1 and A[0][j]==0: dp[0][j] = 1
            else: dp[0][j] = 0
                
        for i in range(1, m):
            for j in range(1, n):
                if A[i][j]==0: dp[i][j] += (dp[i-1][j]+dp[i][j-1])
        return dp[-1][-1]