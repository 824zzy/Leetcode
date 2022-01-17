""" https://leetcode.com/problems/n-th-tribonacci-number/
dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
"""
class Solution:
    def tribonacci(self, n: int) -> int:
        @cache
        def dfs(n):
            if n==0: return 0
            elif n==1: return 1
            elif n==2: return 1
            return dfs(n-1)+dfs(n-2)+dfs(n-3)
        return dfs(n)

        
class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0] * max(4, n+1)
        dp[0], dp[1], dp[2] = 0, 1, 1
        if n<3: return dp[n]
        for i in range(3, n+1):
            dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
        return dp[-1]