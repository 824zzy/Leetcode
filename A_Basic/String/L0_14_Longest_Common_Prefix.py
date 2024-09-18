""" https://leetcode.com/problems/longest-common-prefix/
simulation
"""

from header import *


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        for c in zip(*strs):
            if len(set(c)) != 1:
                return ans
            else:
                ans += c[0]
        return ans
