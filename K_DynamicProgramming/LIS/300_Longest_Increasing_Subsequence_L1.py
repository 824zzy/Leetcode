""" https://leetcode.com/problems/longest-increasing-subsequence/
one of the most famous leetcode problem,
dp[i] denotes length of the longest subsequence from beginning & ending at ith element.
Time complexity: O(N^2)
"""
# bottom up solution
class Solution:
    def lengthOfLIS(self, A: List[int]) -> int:
        dp = [1] * len(A)
        for i in range(1, len(A)):
            for j in range(i):
                if A[j]<A[i]:
                    dp[i] = max(dp[i], dp[j]+ 1)
        return max(dp)

        
# top down solution
class Solution:
    def lengthOfLIS(self, A: List[int]) -> int:
        @cache
        def dp(i):
            if i==len(A): return 0
            ans = 1
            for j in range(i):
                if A[j]<A[i]:
                    ans = max(ans, 1+dp(j))
            return ans
        
        return max(dp(i) for i in range(len(A)))