""" https://leetcode.com/problems/determine-if-two-strings-are-close/description/
hash table + counting
Observation: two strings are close iff they have the same set of characters and the same number of each character.
"""
from header import *


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return sorted(Counter(word1).values()) == sorted(
            Counter(word2).values()) and Counter(word1).keys() == Counter(word2).keys()
