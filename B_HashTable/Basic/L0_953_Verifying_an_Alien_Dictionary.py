""" https://leetcode.com/problems/verifying-an-alien-dictionary/
1. use a map to convert alien to english
2. check if the converted words are sorted
"""
from header import *


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mp = {order[i]: chr(i + 97) for i in range(26)}
        A = ["".join(mp[c] for c in w) for w in words]
        return A == sorted(A)
