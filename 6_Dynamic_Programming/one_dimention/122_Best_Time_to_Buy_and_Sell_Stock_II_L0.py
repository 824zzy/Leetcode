# Facebook
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                p = prices[i+1] - prices[i]
                max_p += p
        return max_p

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp = [0] * len(prices)
        dp[0] = 0
        for i in range(1, len(prices)):
            if prices[i]>prices[i-1]:
                dp[i] = dp[i-1] + prices[i]-prices[i-1]
            else:
                dp[i] = dp[i-1]
        return dp[-1]