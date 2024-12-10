""" https://leetcode.com/problems/two-best-non-overlapping-events/
data structure (binary search) optimized DP
"""

from header import *


class Solution:
    def maxTwoEvents(self, A: List[List[int]]) -> int:
        A.sort()

        @cache
        def dp(i, x):
            if x == 0 or i == len(A):
                return 0
            # skip
            ans = dp(i + 1, x)
            # choose
            j = bisect_right(A, [A[i][1], inf, inf])
            ans = max(ans, A[i][2] + dp(j, x - 1))
            return ans

        return dp(0, 2)
