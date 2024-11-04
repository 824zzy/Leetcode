""" https://leetcode.com/problems/sorting-three-groups/
LIS template
"""

from header import *


class Solution:
    def minimumOperations(self, A: List[int]) -> int:
        dp = [1] * len(A)
        for i in range(len(A)):
            for j in range(i):
                if A[j] <= A[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return len(A) - max(dp)
