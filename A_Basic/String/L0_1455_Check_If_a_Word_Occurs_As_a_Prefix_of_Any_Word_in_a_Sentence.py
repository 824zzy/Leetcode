""" https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/
use startswith or string slicing
"""


class Solution:
    def isPrefixOfWord(self, S: str, pref: str) -> int:
        for i, w in enumerate(S.split()):
            if w.startswith(pref):
                return i + 1
        return -1
