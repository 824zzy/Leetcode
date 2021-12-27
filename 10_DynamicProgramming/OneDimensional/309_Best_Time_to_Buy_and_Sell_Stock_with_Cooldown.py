""" L1: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
transition equation:
    buy[i]  = max(rest[i-1] - A[i], buy[i-1]) 
    sell[i] = max(buy[i-1] + A[i], sell[i-1])
    rest[i] = max(sell[i-1], buy[i-1], rest[i-1])
"""
class Solution:
    def maxProfit(self, A: List[int]) -> int:
        buy = [float('-inf')] * len(A)
        sell = [float('-inf')] * len(A)
        rest = [float('-inf')] * len(A)
        buy[0] = -A[0]
        sell[0] = 0
        rest[0] = 0
        for i in range(1, len(A)):
            buy[i]  = max(rest[i-1] - A[i], buy[i-1]) 
            sell[i] = max(buy[i-1] + A[i], sell[i-1])
            rest[i] = max(sell[i-1], buy[i-1], rest[i-1])
        return sell[-1]