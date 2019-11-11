# Amazon: TODO:
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [amount+1] * (amount+1)
        dp[0] = 0

        for amount in range(1, amount+1):
            for coin in coins:
                if amount-coin >= 0:
                    dp[i] = min(dp[i], 1+dp[amount-coin])
                else:
                    break
        
        if dp[amount] > amount:
            return -1
        else:
            return dp[amount]