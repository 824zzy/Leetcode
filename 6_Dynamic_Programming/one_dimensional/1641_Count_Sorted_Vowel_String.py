""" L2: DP
If k = 1, use only u
If k = 2, use only o,u
If k = 3, use only i,o,u
If k = 4, use only e,i,o,u
If k = 5, use only a,e,i,o,u
"""
class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [1] * 5
        for _ in range(n):
            for i in range(1, 5):
                dp[i] += dp[i-1]
        return dp[-1]