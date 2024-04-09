""" https://leetcode.com/problems/scramble-string/
A special double sequence dp problem using string rather than index.

For every index that we can split the string into two parts, we can either swap the two parts, or keep the two parts the same.
"""
from header import *


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @cache
        def dp(s1, s2):
            if len(s1) == 1:
                return s1 == s2
            if sorted(s1) != sorted(s2):
                return False  # pruning
            ans = False
            for i in range(1, len(s1)):
                ans |= dp(s1[:i], s2[:i]) & dp(s1[i:], s2[i:])
                ans |= dp(s1[:i], s2[-i:]) & dp(s1[i:], s2[:-i])
            return ans

        return dp(s1, s2)
