""" L2: https://leetcode.com/problems/perfect-squares/submissions/
check all the perfect square from i+j*j<=n
and update by min(dp[i+j*j], dp[i] + 1);

Note that j**2 is slower than j*j.
"""
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(n+1):
            j = 1
            while i+j*j <= n:
                dp[i+j*j] = min(dp[i+j*j], dp[i] + 1);
                j += 1
        return dp[-1]