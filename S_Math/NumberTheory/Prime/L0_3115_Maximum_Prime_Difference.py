""" https://leetcode.com/problems/maximum-prime-difference/
1. Sieve of Eratosthenes to find all primes up to 100
2. Find the leftmost and rightmost prime in the list
"""

from header import *


class Solution:
    def maximumPrimeDifference(self, A: List[int]) -> int:
        # Sieve of Eratosthenes
        def findPrimes(n):
            sieve = [1] * n
            sieve[0] = sieve[1] = 0
            for i in range(int(sqrt(n)) + 1):
                if sieve[i]:
                    for j in range(i * i, n, i):
                        sieve[j] = 0
            return sieve

        sieve = findPrimes(101)
        l, r = 0, len(A) - 1
        while sieve[A[l]] == 0:
            l += 1
        while sieve[A[r]] == 0:
            r -= 1
        return r - l
