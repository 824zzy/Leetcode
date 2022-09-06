""" https://leetcode.com/problems/shifting-letters/
One pass to count suffix sum of shifts.
One pass to shift letters in string S
"""
from header import *

class Solution:
    def shiftingLetters(self, s: str, A: List[int]) -> str:
        prefix = list(accumulate(A[::-1]))[::-1]
        ans = []
        for i in range(len(s)):
            c = ord(s[i])-97
            newc = (c+prefix[i])%26
            newc = chr(newc+97)
            ans.append(newc)
        return ''.join(ans)