""" https://leetcode.com/problems/find-and-replace-pattern/
use two hash table to check if their mapping is the same
"""
from header import *


class Solution:
    def findAndReplacePattern(self, words: List[str], P: str) -> List[str]:
        ans = []
        for w in words:
            if len(w) != len(P):
                continue
            x2y, y2x = {}, {}
            for x, y in zip(w, P):
                x2y.setdefault(x, y)
                y2x.setdefault(y, x)
                if x2y[x] != y or y2x[y] != x:
                    break
            else:
                ans.append(w)
        return ans
