""" https://leetcode.com/problems/prime-in-diagonal/
1. collect all diagonal elements
2. find the largest prime among them
"""

from header import *


class Solution:
    def diagonalPrime(self, A: List[List[int]]) -> int:
        def is_prime(n):
            if n <= 1:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        cands = []
        for i in range(len(A)):
            for j in range(len(A)):
                if i == j or i + j == len(A) - 1:
                    cands.append(A[i][j])
        for x in sorted(cands, reverse=True):
            if is_prime(x):
                return x
        return 0
