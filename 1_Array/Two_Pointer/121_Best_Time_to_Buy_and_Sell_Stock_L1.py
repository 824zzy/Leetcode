# Facebook
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:
            return 0
        buy, sell = prices[0], prices[0]
        value = 0
        for i in range(1, len(prices)):
            if prices[i]<buy:
                buy = prices[i]
                sell = prices[i]
            if prices[i]>sell:
                sell = prices[i]
                value = max(value, sell-buy)
        return value 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        ans = 0
        while r<len(prices):
            if prices[l]>prices[r]:
                l = r
                r += 1
            else:
                ans = max(ans, prices[r]-prices[l])
                r += 1
        return ans