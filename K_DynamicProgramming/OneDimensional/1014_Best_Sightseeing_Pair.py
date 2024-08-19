""" https://leetcode.com/problems/best-sightseeing-pair/
"""

from header import *


class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        ans = val = 0
        for i, x in enumerate(A):
            ans = max(ans, x - i + val)
            val = max(val, x + i)
        return ans


class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        @cache
        def dp(i):
            print(i)
            ans = A[i] + max(dp_left(i - 1), dp_right(i + 1))
            return ans

        @cache
        def dp_left(i):
            if i < 0:
                return 0
            return max(dp(i), dp_left(i - 1) - 1)

        @cache
        def dp_right(i):
            if i > len(A) - 1:
                return 0
            return max(dp(i), dp_right(i + 1) - 1)

        return max(dp(i) for i in range(len(A)))
