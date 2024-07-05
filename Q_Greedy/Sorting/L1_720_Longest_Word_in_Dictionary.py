""" https://leetcode.com/problems/longest-word-in-dictionary/submissions/
sort and check if the prefix is in the set
"""
from header import *


class Solution:
    def longestWord(self, W: List[str]) -> str:
        W.sort()
        seen = {""}
        ans = ""
        for w in W:
            if w[:-1] in seen:
                seen.add(w)
                ans = max(ans, w, key=len)
        return ans
