""" https://leetcode.com/problems/reconstruct-original-digits-from-english/
The order of digits is the key to solve problem.
Go through the digits in order, and remove the letters from the string.
"""
from header import *


class Solution:
    def originalDigits(self, s: str) -> str:
        mp = [('zero', 'z', 0),
              ('two', 'w', 2),
              ('six', 'x', 6),
              ('four', 'u', 4),
              ('one', 'o', 1),
              ('eight', 'g', 8),
              ('five', 'f', 5),
              ('nine', 'i', 9),
              ('seven', 's', 7),
              ('three', 'r', 3)]
        cnt = Counter(s)
        ans = [0] * 10
        for d, c, n in mp:
            ans[n] += cnt[c]
            cnt -= Counter(d * cnt[c])
        return ''.join([str(i) * c for i, c in enumerate(ans) if c != 0])
