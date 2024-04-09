""" https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/
array counting

count differences:
1. in S but not in T, in T but not in S
2. overlap's difference
"""
from header import *


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cntS, cntT = Counter(s), Counter(t)
        ans = 0
        for ks, vs in cntS.items():
            if ks not in cntT:  # find diff
                ans += vs
        for kt, vt in cntT.items():
            if kt not in cntS:  # find diff
                ans += vt
            else:  # find overlap
                ans += abs(vt - cntS[kt])
        return ans // 2
