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

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        ans = set()
        for x in nums:
            d = 2
            while d*d<=x:
                if x%d==0:
                    ans.add(d)
                    x //= d
                    while x%d==0:
                        x //= d
                d += 1
            if x>1:
                ans.add(x)
        return len(ans)