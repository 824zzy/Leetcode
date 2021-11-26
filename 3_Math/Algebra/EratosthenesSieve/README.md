# Sieve of Eratosthenes

In mathematics, the sieve of Eratosthenes is an ancient algorithm for finding all prime numbers up to any given limit.
It works by iteratively marking multiples of prime factors non-prime:
    `Go over i from 2 to sqrt(n)+1. If i is a prime, then i*i, i*(i+1), i*(i+2), etc. are not primes`

## Template

```py
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
```

## Reference

- [wiki: Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
