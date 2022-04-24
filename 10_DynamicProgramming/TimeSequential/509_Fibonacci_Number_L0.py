""" L0: https://leetcode.com/problems/fibonacci-number/
classical textbook problem
"""
# bottom up solution
class Solution:
    def fib(self, n: int) -> int:
        if n<2: return n
        dp = [0] * (n+1)
        dp[0], dp[1] = 0, 1
        for i in range(2, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[-1]
    
# top down solution
class Solution:
    def fib(self, n: int) -> int:
        @cache
        def dfs(n):
            if n==0: return 0
            if n==1: return 1
            return dfs(n-1)+dfs(n-2)
        return dfs(n)