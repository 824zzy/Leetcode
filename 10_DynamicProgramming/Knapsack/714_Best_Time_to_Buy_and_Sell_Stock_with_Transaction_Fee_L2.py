""" https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
three states: skip / sell / buy with fee
"""
class Solution:
    def maxProfit(self, A: List[int], fee: int) -> int:
        @cache
        def dfs(i, can):
            if i>=len(A): return 0
            ans = dfs(i+1, can) # skip
            if not can: ans = max(ans, A[i]+dfs(i+1, 1)) # sell
            return max(ans, -A[i]-fee+dfs(i+1, 0)) # buy
        
        return dfs(0, 1)
    
class Solution:
    def maxProfit(self, A: List[int], f: int) -> int:
        dp_s = [0] * len(A)
        dp_h = [0] * len(A)
        dp_h[0] = -A[0]
        for i in range(1, len(A)):
            dp_s[i] = max(dp_s[i-1], dp_h[i-1]+A[i]-f)
            dp_h[i] = max(dp_h[i-1], dp_s[i-1]-A[i])
        return dp_s[-1]