""" https://leetcode.com/problems/find-xor-beauty-of-array/
formulate answer bit by bit:
 ((a | b) & c) = 1
 ==> c = 1, a|b = 1
 ==> a or b = 1
 suppose the i-th bit position has y 1bit and n-y 0bit.
    ones = (n^2-(n-y)^2)*y = 2ny^2 - y^3
    ==> only y's parity matters
"""
from header import *
from functools import reduce


class Solution:
    def xorBeauty(self, A: List[int]) -> int:
        return reduce(xor, A)
