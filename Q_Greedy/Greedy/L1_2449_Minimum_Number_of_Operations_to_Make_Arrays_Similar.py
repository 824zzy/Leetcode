""" https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/
sort two arrays by parity, then greedily sum up the positive difference
"""
from header import *


class Solution:
    def makeSimilar(self, A: List[int], T: List[int]) -> int:
        A_odd = sorted([x for x in A if x & 1])
        A_even = sorted([x for x in A if x & 1 == 0])
        T_odd = sorted([x for x in T if x & 1])
        T_even = sorted([x for x in T if x & 1 == 0])

        ans = 0
        for i, j in zip(A_odd, T_odd):
            if (i - j) > 0:
                ans += (i - j)
        for i, j in zip(A_even, T_even):
            if (i - j) > 0:
                ans += (i - j)
        return ans // 2
