class Solution:
    def fib(self, N: int) -> int:
        if N==0:
            return 0
        dp = [0] * (N+1)
        dp[1] = 1
        for i in range(2, N+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[N]