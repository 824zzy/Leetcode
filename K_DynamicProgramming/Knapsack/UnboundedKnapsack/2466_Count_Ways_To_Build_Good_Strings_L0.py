""" https://leetcode.com/problems/count-ways-to-build-good-strings/description/
"""
from header import *

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        @cache
        def dp(i):
            if i>high: return 0
            return (i>=low)+dp(i+zero)+dp(i+one)%(10**9+7)
        return dp(0)%(10**9+7)