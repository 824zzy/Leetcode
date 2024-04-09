""" https://leetcode.com/problems/4-keys-keyboard/
TODO:
"""
from header import *


class Solution:
    def maxA(self, n: int) -> int:
        @cache
        def dp(n):
            if n <= 1:
                return n
            # skip
            ans = dp(n - 1) + 1
            # copy
            for x in range(n - 2):
                ans = max(ans, dp(x) * (n - x - 1))
            return ans

        return dp(n)
