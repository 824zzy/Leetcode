""" https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/
prefix suffix decomposition + LIS template (either DP or binary search)
"""

from header import *


class Solution:
    def minimumMountainRemovals(self, A: List[int]) -> int:
        def LIS(A):
            dp = [1] * len(A)
            for i in range(len(A)):
                for j in range(i):
                    if A[j] < A[i]:
                        dp[i] = max(dp[i], dp[j] + 1)
            return dp

        pre = LIS(A)
        suf = LIS(A[::-1])[::-1]
        ans = inf

        for i in range(1, len(A) - 1):
            if pre[i] == 1 or suf[i] == 1:
                continue
            ans = min(ans, len(A) - (pre[i] + suf[i] - 1))
        return ans


"""
[1,3,1]
[2,1,1,5,6,2,3,1]
[9,8,1,7,6,5,4,3,2,1]
[100,92,89,77,74,66,64,66,64]
"""
