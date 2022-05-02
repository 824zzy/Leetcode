""" https://leetcode.com/problems/count-primes/
Template: Sieve of Eratosthenes
"""
from math import sqrt
class Solution:
    def countPrimes(self, idx):
        n = 21000
        sieve = [1]*n
        sieve[0] = sieve[1] = 0
        for i in range(int(sqrt(n))+1):
            if sieve[i]:
                for j in range(i*i, n, i): 
                    sieve[j] = 0
        
        ans = ''
        for i in range(n):
            if sieve[i]: ans += str(i)
        return ans[idx:idx+5]        

s = Solution()
ans = s.countPrimes(1000)
print(ans)