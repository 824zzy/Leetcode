""" https://leetcode.com/problems/minimum-cost-to-cut-a-stick/
similar to 1000. Minimum Cost to Merge Stones

time complexity: O(L^3)
"""
from header import *


class Solution:
    def minCost(self, n: int, A: List[int]) -> int:
        A.extend([0, n])
        A.sort()

        @cache
        def dp(l, r):
            if l + 1 == r:
                return 0
            ans = inf
            for x in range(l + 1, r):
                ans = min(ans, A[r] - A[l] + dp(l, x) + dp(x, r))
            return ans

        return dp(0, len(A) - 1)
