""" https://leetcode.com/problems/make-array-strictly-increasing/
change or not to change the i-th element
"""
from header import *


class Solution:
    def makeArrayIncreasing(self, A: List[int], B: List[int]) -> int:
        B.sort()

        @cache
        def dp(i, prev):
            if i == len(A):
                return 0
            ans = inf
            # don't change i-th element
            if A[i] > prev:
                ans = dp(i + 1, A[i])
            # change i-th element to the prev's nearest element in B
            k = bisect_right(B, prev)
            if k < len(B):
                ans = min(ans, 1 + dp(i + 1, B[k]))
            return ans

        ans = dp(0, -inf)
        return dp(0, -inf) if ans != inf else -1
