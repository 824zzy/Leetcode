""" L2: LIS problem
dp[i] denotes length of the longest subsequence from begining & ending at ith element
"""
class Solution:
    def lengthOfLIS(self, A: List[int]) -> int:
        dp = [1 for _ in range(len(A)+1)]
        ans = 0
        for i in range(1, len(A)):
            for j in range(i):
                if A[j]<A[i]:
                    dp[i] = max(dp[i], dp[j]+1)
            ans = max(ans, dp[i])
        return ans