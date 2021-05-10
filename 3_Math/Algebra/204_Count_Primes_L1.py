"""
Sieve of Eratosthenes
"""
class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [1] * n
        ans = 0
        for i in range(2, n):
            if not prime[i]: continue
            ans += 1 
            for j in range(2, n//i+1):
                if i*j<n: prime[i*j] = 0
        return ans