""" https://leetcode.com/problems/closest-prime-numbers-in-range/
1. use Sieve of Eratosthenes to find all the prime less than right+1
2. two pointers to find the closest prime numbers
"""
from header import *


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        sieve = [1] * (right + 1)
        sieve[0] = sieve[1] = 0
        for i in range(int(sqrt(right + 1)) + 1):
            if sieve[i]:
                for j in range(i * i, right + 1, i):
                    sieve[j] = 0

        i = None
        ans = [-inf, inf]
        for j in range(left, len(sieve)):
            if sieve[j] == 1:
                if i:
                    ans = min(ans, [i, j], key=lambda x: x[1] - x[0])
                i = j
        return ans if ans != [-inf, inf] else [-1, -1]
