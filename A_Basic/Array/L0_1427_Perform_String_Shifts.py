""" https://leetcode.com/problems/perform-string-shifts/
"""
from header import *


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        x = 0
        for d, a in shift:
            if d == 0:
                x += a
            else:
                x -= a
        x %= len(s)
        return s[x:] + s[:x]


"""
"abc"
[[0,1],[1,2]]
"abcdefg"
[[1,1],[1,1],[0,2],[1,3]]
"joiazl"
[[1,1],[1,6],[0,1],[1,3],[1,0],[0,3]]
"wpdhhcj"
[[0,7],[1,7],[1,0],[1,3],[0,3],[0,6],[1,2]]
"""
