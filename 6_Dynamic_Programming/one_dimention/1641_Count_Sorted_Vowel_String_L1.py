class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [1] * 5
        for _ in range(n):
            for i in range(1, 5):
                dp[i] += dp[i-1]
        return dp[-1]