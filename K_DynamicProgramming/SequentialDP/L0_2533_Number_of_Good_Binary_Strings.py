""" https://leetcode.com/problems/number-of-good-binary-strings/
"""
from header import *


class Solution:
    def goodBinaryStrings(self, mn: int, mx: int, ones: int, zeros: int) -> int:
        @cache
        def dp(i):
            if i > mx:
                return 0
            return ((mn <= i <= mx) + dp(i + ones) + dp(i + zeros)) % (10 ** 9 + 7)

        return dp(0)
