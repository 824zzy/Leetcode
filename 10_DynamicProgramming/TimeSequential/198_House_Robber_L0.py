""" https://leetcode.com/problems/house-robber/
max(dp[i-1], A[i-1]+dp[i-2])
"""
# top down
class Solution:
    def rob(self, A: List[int]) -> int:
        @cache
        def dfs(i):
            if i<0: return 0
            return max(dfs(i-2)+A[i], dfs(i-1))
        
        return dfs(len(A)-1)
    
# bottom up
class Solution:
    def rob(self, A: List[int]) -> int:
        dp = [0] * (len(A)+1)
        dp[1] = A[0]
        for i in range(2, len(A)+1):
            dp[i] = max(dp[i-1], A[i-1]+dp[i-2])
        return dp[-1]