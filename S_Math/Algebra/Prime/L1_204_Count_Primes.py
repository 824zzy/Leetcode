""" https://leetcode.com/problems/count-primes/
Template: Sieve of Eratosthenes
"""
from header import *

class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2: return 0
        
        sieve = [1]*n
        sieve[0] = sieve[1] = 0
        for i in range(int(sqrt(n))+1):
            if sieve[i]:
                for j in range(i*i, n, i): 
                    sieve[j] = 0
        return sum(sieve)