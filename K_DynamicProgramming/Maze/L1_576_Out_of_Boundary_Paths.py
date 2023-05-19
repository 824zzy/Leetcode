""" https://leetcode.com/problems/out-of-boundary-paths/
the answer needs modulo 10^9 + 7 is a hint to use dp, so just apply maze dp to find the answer

Time complexity: O(m*n*maxMove*4) ~= 5 * 10^6
"""
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        @cache
        def dp(x, y, step):
            if not (0<=x<m and 0<=y<n): return 1
            if not step:  return 0
            
            ans = 0
            for dx, dy in D:
                ans += dp(x+dx, y+dy, step-1)
            return ans%(10**9+7)
        
        return dp(startRow, startColumn, maxMove)%(10**9+7)
    
# bottom up
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