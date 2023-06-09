""" https://leetcode.com/problems/find-smallest-letter-greater-than-target/
find smallest letter greater than target using binary search
"""
from header import *

class Solution:
    def nextGreatestLetter(self, L: List[str], t: str) -> str:
        i = bisect_right(L, t)
        if i==len(L):
            return L[0]
        return L[bisect_right(L, t)]