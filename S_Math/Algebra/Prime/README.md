# Prime Number

## Large Prime Optimization

**A number can have at most one prime factor that is greater than its square root.** E.g.: 2521

``` py
# find all prime factors less than sqrt(max(nums))
ans = set()
for p in primes:
    if n%p == 0:
        ans.add(p)
        while n%p == 0:
            n //= p
# find a large prime
if n!=1: ans.add(n)
```

## Sieve of Eratosthenes

In mathematics, the sieve of Eratosthenes is an ancient algorithm for finding all prime numbers up to any given limit.
It works by iteratively marking multiples of prime factors non-prime:
    `Go over i from 2 to sqrt(n)+1. If i is a prime, then i*i, i*(i+1), i*(i+2), etc. are not primes`

## Template

```py
# count primes less than n
def countPrimes(n):
    if n<2: return 0
    
    sieve = [1]*n
    sieve[0] = sieve[1] = 0
    for i in range(int(sqrt(n))+1):
        if sieve[i]:
            for j in range(i*i, n, i): 
                sieve[j] = 0
    return sum(sieve)

# find primes less than n
def findPrimes(n):
    if n<2: return 0
    
    sieve = [1]*n
    sieve[0] = sieve[1] = 0
    for i in range(int(sqrt(n))+1):
        if sieve[i]:
            for j in range(i*i, n, i): 
                sieve[j] = 0
    return [i for i in range(n) if sieve[i]]
```

## Reference

- [wiki: Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
