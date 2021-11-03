""" L1: https://leetcode.com/problems/unique-paths-ii/
"""
# top-down solution from end point
class Solution:
    def uniquePathsWithObstacles(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0]) # dimensions 
        
        @cache
        def dfs(i, j):
            if A[i][j] or i < 0 or j < 0: return 0 
            if i == j == 0: return 1
            return dfs(i-1, j)+dsf(i, j-1)
        
        return dfs(m-1, n-1)
    
# top-down solution from start point
class Solution:
    def uniquePathsWithObstacles(self, A: List[List[int]]) -> int:
        M, N = len(A), len(A[0])
        if A[0][0]==1 or A[M-1][N-1]==1: return 0
        @cache
        def dfs(x, y):
            if [x, y]==[M-1, N-1]: return 1
            ans = 0
            for dx, dy in [(0, 1), (1, 0)]:
                if 0<=x+dx<M and 0<=y+dy<N and A[x+dx][y+dy]==0:
                    ans += dfs(x+dx, y+dy)
            return ans
        return dfs(0, 0)
    
# bottom up solution
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