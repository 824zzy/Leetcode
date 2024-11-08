""" https://leetcode.com/problems/number-of-laser-beams-in-a-bank/
simulate laser beam row by row
"""

from header import *


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        for x, y in pairwise([x.count("1") for x in bank if x.count("1")]):
            ans += x * y
        return ans
