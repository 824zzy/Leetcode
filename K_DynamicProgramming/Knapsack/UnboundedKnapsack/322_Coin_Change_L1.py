""" https://leetcode.com/problems/coin-change/
time-dependent/unbounded knap sack problem.
"""
# top down
class Solution:
    def coinChange(self, A: List[int], n: int) -> int:
        @cache
        def dp(n):
            if n==0: return 0
            elif n<0: return inf
            return min(1+dp(n-c) for c in A)
        
        ans = dp(n)
        return -1 if ans==inf else ans


# another top down implementation
class Solution:
    def coinChange(self, A: List[int], n: int) -> int:
        A.sort(reverse=True)
        
        @cache
        def dp(i, rm):
            if rm==0: return 0
            elif rm<0: return inf
            elif i==len(A): return inf
            return min(1+dp(i, rm-A[i]), dp(i+1, rm))
        
        ans = dp(0, n)
        if ans!=inf: return ans
        else: return -1
    
    
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