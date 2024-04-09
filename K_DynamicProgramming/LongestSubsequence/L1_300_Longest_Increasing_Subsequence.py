""" https://leetcode.com/problems/longest-increasing-subsequence/
one of the most famous leetcode problem,
dp[i] denotes length of the longest subsequence from beginning & ending at ith element.
Time complexity: O(N^2)
"""
from header import *

# bottom up solution


class Solution:
    def lengthOfLIS(self, A: List[int]) -> int:
        dp = [1] * len(A)
        for i in range(1, len(A)):
            for j in range(i):
                if A[j] < A[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


# top down solution
class Solution:
    def lengthOfLIS(self, A: List[int]) -> int:
        @cache
        def dp(i):
            ans = 1
            for j in range(i):
                if A[j] < A[i]:
                    ans = max(ans, 1 + dp(j))
            return ans

        return max(dp(i) for i in range(len(A)))


# binary search solution: use bisect to maintain a increasing list
class Solution:
    def lengthOfLIS(self, A: List[int]) -> int:
        vals = []
        for x in A:
            k = bisect_left(vals, x)
            if k == len(vals):
                vals.append(x)
            else:
                vals[k] = x
        return len(vals)
