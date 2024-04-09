""" https://leetcode.com/problems/license-key-formatting/
simulation
"""
from header import *


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = ''.join(s.split('-'))[::-1]
        ans = []
        for i in range(0, len(s), k):
            ans.append(s[i:i + k].upper()[::-1])
        return '-'.join(ans[::-1])
