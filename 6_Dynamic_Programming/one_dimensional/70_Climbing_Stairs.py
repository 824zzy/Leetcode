""" L0: https://leetcode.com/problems/climbing-stairs/
1. dp[0] = 1, dp[1] = 2
2. dp[i] = dp[i-1] + dp[i-2]; (i>=2)
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        dp = [0] * n
        dp[0], dp[1] = 1, 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]

# top down solution
class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(None)
        def dfs(idx):
            if idx<2: return 1
            return dfs(idx-1)+dfs(idx-2)
        return dfs(n)