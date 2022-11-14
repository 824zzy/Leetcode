""" https://leetcode.com/problems/count-ways-to-build-good-strings/description/
"""
from header import *

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        @cache
        def dp(l):
            ans = 0
            if low<=l<=high: ans += 1
            if l+zero<=high:
                ans += dp(l+zero)
            if l+one<=high:
                ans += dp(l+one)
            return ans%(10**9+7)
        
        return dp