""" https://leetcode.com/problems/minimum-number-of-keypresses/
1. sort the characters in the string by their frequency.
2. count keypress time
"""
from header import *
class Solution:
    def minimumKeypresses(self, s: str) -> int:
        A = sorted(Counter(s).items(), key=lambda x: -x[1])
        ans = 0
        i = 0
        for i, (_, v) in enumerate(A):
            ans += (i//9+1)*v
        return ans