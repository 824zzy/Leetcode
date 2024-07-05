""" https://leetcode.com/problems/merge-strings-alternately
basic usage of zip_longest
"""
from header import *


class Solution:
    def mergeAlternately(self, x: str, y: str) -> str:
        ans = ""
        for xx, yy in zip_longest(x, y, fillvalue=""):
            ans += xx
            ans += yy
        return ans


# linear scan
class Solution:
    def mergeAlternately(self, A: str, B: str) -> str:
        A, B = list(A), list(B)
        ans = ""
        while A or B:
            if A:
                ans += A.pop(0)
            if B:
                ans += B.pop(0)
        return ans
