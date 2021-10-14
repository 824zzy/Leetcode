""" L2: https://leetcode.com/problems/perfect-squares/submissions/
check all the perfect square from i+j**2<=n
and update by min(dp[i+j**2], dp[i] + 1);
"""
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(n+1):
            j = 1
            while i+j**2 <= n:
                dp[i+j**2] = min(dp[i+j**2], dp[i]+1);
                j += 1
        return dp[-1]