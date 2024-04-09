class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * n
        dp[0] = dp[1] = 1
        for i in range(2, n):
            for j in range(i):
                dp[i] = max(dp[i], (j + 1) * max(dp[i - j - 1], i - j))
        return dp[-1]
