""" https://leetcode.com/problems/frog-jump/
dp + pruning

Solution 1: define dp state as dp[i][k], where i is the index of the stone, k is the last jump distance
Solution 2: define dp state as dp[i][k], where x is the current position's unit, k is the last jump distance
"""
from header import *


class Solution:
    def canCross(self, A: List[int]) -> bool:
        if A[1] != 1:
            return False

        @cache
        def dp(i, k):
            if i == len(A) - 1:
                return True
            ans = False
            for j in range(i + 1, len(A)):
                if abs(A[j] - A[i] - k) <= 1:
                    ans |= dp(j, A[j] - A[i])
                elif A[j] - A[i] - k > 1:
                    break
            return ans

        return dp(1, 1)


class Solution:
    def canCross(self, A: List[int]) -> bool:
        if A[1] != 1:
            return False
        _A = set(A)

        @cache
        def dp(x, k):
            if x == A[-1]:
                return True
            ans = False
            for kk in (k - 1, k, k + 1):
                if kk > 0 and x + kk in _A:
                    ans |= dp(x + kk, kk)
            return ans

        return dp(1, 1)
