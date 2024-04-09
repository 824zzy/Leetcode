""" https://leetcode.com/problems/number-of-even-and-odd-bits/
simulation by bit manipulation
"""
from header import *


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        odd, even = 0, 0
        i = 0
        while n:
            if n & 1:
                if i == 0:
                    even += 1
                else:
                    odd += 1
            i ^= 1
            n >>= 1
        return [even, odd]
