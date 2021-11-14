""" From lee215
dp[i] means the result for n = i.

if there is any k that dp[i - k * k] == false,
it means we can make the other lose the game,
so we can win the game an dp[i] = true.
"""
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(1, n+1):
            for k in range(1, int(i**0.5)+1):
                if k*k<=i and dp[i-k*k]==0:
                    dp[i] = 1
        return dp[n]