""" https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
Counter comparison
"""
from header import *


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cnt = Counter(chars)
        ans = 0
        for w in words:
            if cnt >= Counter(w):
                ans += len(w)
        return ans
