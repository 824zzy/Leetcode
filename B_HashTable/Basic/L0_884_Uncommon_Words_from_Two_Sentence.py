""" https://leetcode.com/problems/uncommon-words-from-two-sentences/
translate the problem into find the words that only appear in both s1 and s2
"""
from header import *


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s = s1 + ' ' + s2
        return [k for k, v in Counter(s.split()).items() if v == 1]
