""" https://leetcode.com/problems/two-best-non-overlapping-events/

"""
from header import *


class Solution:
    def maxTwoEvents(self, A: List[List[int]]) -> int:
        A.sort()

        @cache
        def dp(i, n):
            if n == 0 or i == len(A):
                return 0
            ans = dp(i + 1, n)
            nxt = bisect_left(A, [A[i][1] + 1, 0, 0])
            ans = max(ans, A[i][2] + dp(nxt, n - 1))
            return ans

        return dp(0, 2)
