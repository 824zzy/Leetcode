""" https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/
large prime optimization:
    - only focus on primes up to sqrt(max(nums))
"""
from header import *

# large prime optimization
class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}
        ans = set()
        for n in nums:
            for p in primes:
                if n%p == 0:
                    ans.add(p)
                    while n%p == 0:
                        n //= p
            # find a large prime
            if n!=1: ans.add(n)
        return len(ans)

# brute force
class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def primeFactors(n):
            c = 2
            ans = set()
            while n>1:
                if n%c==0:
                    ans.add(c)
                    n //= c
                else:
                    c += 1
            return ans
        
        ans = set()
        for n in nums:
            ans |= primeFactors(n)
        return len(ans)
        
"""
[2,4,3,7,10,6]
[2,4,8,16]
[3]
"""