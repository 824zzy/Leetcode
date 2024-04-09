""" https://leetcode.com/problems/russian-doll-envelopes/
"""
from header import *


class Solution:
    def maxEnvelopes(self, A: List[List[int]]) -> int:
        A = sorted(A, key=lambda x: (x[0], -x[1]))

        vals = []
        for i in range(len(A)):
            k = bisect_left(vals, A[i][1])
            if k == len(vals):
                vals.append(A[i][1])
            else:
                vals[k] = A[i][1]
        return len(vals)

# DP(N^2) will TLE


class Solution:
    def maxEnvelopes(self, A: List[List[int]]) -> int:
        A = sorted(A, key=lambda x: (x[0], -x[1]))
        dp = [1] * len(A)
        ans = 1
        for i in range(1, len(A)):
            for j in range(i):
                if A[i][1] > A[j][1] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
            if ans < dp[i]:
                ans = dp[i]
        return ans
