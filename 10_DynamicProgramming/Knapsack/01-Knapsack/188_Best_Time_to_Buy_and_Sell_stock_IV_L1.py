""" https://leetcode.com/explore/learn/card/dynamic-programming/632/common-patterns-in-dp-problems/4117/
if one can buy, one can choose to buy or skip
if one cannot buy, one can choose to sell or skip
"""
class Solution:
    def maxProfit(self, k: int, A: List[int]) -> int:
        @cache
        def dfs(i, can, k):
            if i==len(A) or k==0: return 0
            ans = dfs(i+1, can, k) # skip
            if not can: ans = max(ans, A[i]+dfs(i+1, 1, k-1)) # sell
            return max(ans, -A[i]+dfs(i+1, 0, k)) # buy
        
        return dfs(0, 1, k)