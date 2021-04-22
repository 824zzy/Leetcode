# From bottom to up
class Solution:
    def minimumTotal(self, A: List[List[int]]) -> int:
        dp = A[-1]
        for i in range(len(A)-2, -1, -1):
            for j in range(i+1):
                dp[j] = A[i][j] + min(dp[j], dp[j+1])
        return dp[0]