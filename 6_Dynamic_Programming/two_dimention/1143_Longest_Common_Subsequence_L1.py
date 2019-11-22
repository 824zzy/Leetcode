class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        for m in range(1, len(text1)+1):
            for n in range(1, len(text2)+1):
                if text1[m-1]==text2[n-1]:
                    dp[m][n] = min(dp[m-1][n], dp[m-1][n-1], dp[m][n-1]) + 1
                else:
                    dp[m][n] = max(dp[m-1][n], dp[m-1][n-1], dp[m][n-1])
        return dp[-1][-1]
"""
"bsbininm"
"jmjkbkjkv"

"abcde"
"ace"

"abc"
"def"
"""