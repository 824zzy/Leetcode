""" L1: https://leetcode.com/problems/jump-game-ii/
"""
class Solution:
    def jump(self, A: List[int]) -> int:
        dp = [float('inf')] * len(A)
        dp[0] = 0
        for i in range(len(A)):
            for j in range(1, A[i]+1):
                if i+j<len(A): dp[i+j] = min(dp[i+j], dp[i]+1)
        return dp[-1]