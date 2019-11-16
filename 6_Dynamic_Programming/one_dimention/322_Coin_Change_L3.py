# Amazon:
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