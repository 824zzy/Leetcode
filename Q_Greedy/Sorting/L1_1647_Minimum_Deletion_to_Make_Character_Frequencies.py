""" https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
greedily find the smallest number of deletions to make all frequencies unique
"""
from header import *


class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = Counter(s)
        ans = 0
        seen = set()
        for _, f in cnt.items():
            while f > 0 and f in seen:
                f -= 1
                ans += 1
            seen.add(f)
        return ans
