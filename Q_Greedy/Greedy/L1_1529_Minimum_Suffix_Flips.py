""" https://leetcode.com/problems/minimum-suffix-flips/
The flips are only related to the number of groups of 1s and 0s.
If the first group number is 0, then we don't need to flip.
"""
from header import *


class Solution:
    def minFlips(self, A: str) -> int:
        A = [k for k, _ in groupby(A)]
        return len(A) - (A[0] == '0')


"""
"10111"
"101"
"00000"
"111"
"01010101"
"11000"
"""
