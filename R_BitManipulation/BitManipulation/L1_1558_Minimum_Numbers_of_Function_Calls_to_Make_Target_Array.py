""" https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array/
bit simulation
"""
from header import *


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def count(n):
            inc, mul = 0, 0
            while n:
                if n & 1:
                    n -= 1
                    inc += 1
                else:
                    n >>= 1
                    mul += 1
            return inc, mul

        inc, mul = 0, 0
        for n in nums:
            _inc, _mul = count(n)
            inc += _inc
            mul = max(mul, _mul)
        return inc+mul
