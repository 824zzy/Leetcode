""" https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/
use startswith or string slicing
"""


class Solution:
    def isPrefixOfWord(self, S: str, pref: str) -> int:
        for i, w in enumerate(S.split()):
            if w.startswith(pref):
                return i + 1
        return -1


class Solution:
    def isPrefixOfWord(self, A: str, p: str) -> int:
        for i, w in enumerate(A.split()):
            if len(w) >= len(p):
                if w[: len(p)] == p:
                    return i + 1
        return -1
