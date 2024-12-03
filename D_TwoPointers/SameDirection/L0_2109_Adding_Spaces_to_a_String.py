""" https://leetcode.com/problems/adding-spaces-to-a-string/
string simulation using two pointers
"""

from header import *


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ""
        j = 0
        for i, c in enumerate(s):
            if j < len(spaces) and i == spaces[j]:
                ans += " "
                j += 1
            ans += c
        return ans
