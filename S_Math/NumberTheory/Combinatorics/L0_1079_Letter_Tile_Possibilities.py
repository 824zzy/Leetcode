""" https://leetcode.com/problems/letter-tile-possibilities/description/
since n is small, we can find all the permutations and count unique ones.
"""
from header import *


class Solution:
    def numTilePossibilities(self, A: str) -> int:
        ans = []
        for i in range(1, len(A) + 1):
            ans.extend(list(permutations(A, i)))
        return len(set(ans))
