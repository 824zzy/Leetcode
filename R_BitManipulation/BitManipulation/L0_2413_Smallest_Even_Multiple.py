""" https://leetcode.com/problems/smallest-even-multiple/
if n is odd, then the smallest even multiple is 2n
if n is even, then the smallest even multiple is n itself
"""


class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n & 1:
            return n << 1
        else:
            return n

# or simulation


class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        _n = n
        while n % 2 or n % _n:
            n *= 2
        return n
