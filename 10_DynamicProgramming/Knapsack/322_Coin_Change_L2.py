""" https://leetcode.com/problems/coin-change/
time-dependent/complete knap sack.
"""
# top down
class Solution:
    def coinChange(self, A: List[int], n: int) -> int:
        
        @cache
        def dfs(n):
            if n==0: return 0
            elif n<0: return inf
            return min(1+dfs(n-c) for c in A)
        
        ans = dfs(n)
        return -1 if ans==inf else ans
    
    
"""
1. dp[0] = 0, we don't need any coins for 0
2. dp[i] = min(dp[i], 1+dp[i-coin])
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for a in range(1, amount+1):
            for c in coins:
                if a-c>=0:
                    dp[a] = min(dp[a], dp[a-c]+1)
        return dp[-1] if dp[-1]!=float('inf') else -1
    
"""
1. dp[c] = 1
2. do[c+i] = min(dp[c+i], dp[i]+1)
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0: return 0
        dp = [float('inf')] * (amount+1)
        for c in coins: 
            if c<len(dp): dp[c] = 1
        for i in range(1, len(dp)):
            if dp[i]!=float('inf'):
                for c in coins:
                    if c+i<len(dp): dp[c+i] = min(dp[c+i], dp[i]+1)
        
        if dp[-1]!=float('inf'): return dp[-1]
        else: return -1