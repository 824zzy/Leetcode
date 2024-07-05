""" https://leetcode.com/problems/custom-sort-string/
hash table + counting

Use counter and set to formulate string by in order and not in order
"""
from header import *


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cnt = Counter(s)
        ans = ""
        for c in order:
            ans += c * cnt[c]
            if c in cnt:
                cnt.pop(c)
        return ans + "".join([k * v for k, v in cnt.items()])
