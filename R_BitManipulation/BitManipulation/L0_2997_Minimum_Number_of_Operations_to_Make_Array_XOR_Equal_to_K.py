""" https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/submissions/
bit manipulation + simulation
"""
from header import *
from functools import reduce


class Solution:
    def minOperations(self, A: List[int], k: int) -> int:
        x = reduce(xor, A)
        ans = 0
        for x, y in zip(bin(x)[2:].zfill(32), bin(k)[2:].zfill(32)):
            if x != y:
                ans += 1
        return ans


"""
010
001
011
100
100
001
"""
