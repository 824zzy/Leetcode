""" https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/description/
isdigit(): check if all the characters in the string are digits
isnumeric(): check if one character is digit
"""
from header import *


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        ans = 0
        for s in strs:
            if s.isdigit():
                ans = max(ans, int(s))
            else:
                ans = max(ans, len(s))
        return ans
