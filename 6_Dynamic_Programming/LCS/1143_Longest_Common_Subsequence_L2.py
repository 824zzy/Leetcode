class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]
        for i in range(len(A)):
            for j in range(len(B)):
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j], dp[i][j]+(A[i]==B[j]))
        return dp[-1][-1]