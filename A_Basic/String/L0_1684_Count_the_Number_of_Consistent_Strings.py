""" https://leetcode.com/problems/count-the-number-of-consistent-strings/
simulation
"""

from header import *


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a = set(allowed)
        ans = 0
        for w in words:
            if not set(w) - a:
                ans += 1
        return ans
