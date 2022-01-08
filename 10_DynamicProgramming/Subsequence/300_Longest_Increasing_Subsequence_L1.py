""" https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/
dp[i] denotes length of the longest subsequence from begining & ending at ith element
enhanced time sequential
"""
# top down
class Solution:
    def lengthOfLIS(self, A: List[int]) -> int:
        @cache
        def dfs(i):
            if i==len(A): return 0
            return 1+max([dfs(j) for j in range(i) if A[j]<A[i]], default=0)
                
        return max(dfs(i) for i in range(len(A)))

# bottom up
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