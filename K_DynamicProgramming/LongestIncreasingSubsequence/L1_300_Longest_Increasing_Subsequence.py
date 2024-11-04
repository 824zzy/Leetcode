""" https://leetcode.com/problems/longest-increasing-subsequence/
use bisect to maintain a increasing list.
O(NlogN)
"""

from header import *


# O(N^2) DP
class Solution:
    def lengthOfLIS(self, A: List[int]) -> int:
        dp = [1] * len(A)
        for i in range(len(A)):
            for j in range(i):
                if A[j] < A[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


# O(NlogN) binary search + greedy
class Solution:
    def lengthOfLIS(self, A: List[int]) -> int:
        dp = []
        for x in A:
            k = bisect_left(dp, x)
            if k == len(dp):
                dp.append(x)
            else:
                dp[k] = x
        return len(dp)
