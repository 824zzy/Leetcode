""" https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/
translate the problem into: find smallest element in A that is a factor is all the elements of D
1. find gcd of D
2. check if xx is a factor of gcd
"""
from functools import reduce


class Solution:
    def minOperations(self, A: List[int], D: List[int]) -> int:
        A.sort()
        x = reduce(gcd, D)

        for i, xx in enumerate(A):
            if x % xx == 0:
                return i
        return -1
