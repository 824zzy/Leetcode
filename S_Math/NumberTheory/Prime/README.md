# Prime Number

## When to Use

| Problem Signal | Technique |
|---|---|
| Count/find all primes in a range | Sieve of Eratosthenes |
| Find prime factors of a number | Prime factorization (trial division) |
| Numbers up to 10^6, need prime/factor info for all | Least Prime Factor (LPF) precomputation |
| Numbers up to 10^9, need prime factors | Large prime optimization (small primes + one large) |
| Check if single number is prime | Trial division up to sqrt(n) |
| Connect numbers by common factors | Prime factorization + Union Find |
| Track leftmost/rightmost occurrence of each prime | Prime factorization + sweep line |

## Check if a Number is Prime

Key insight: only need to check divisibility up to sqrt(n).

```py
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

LC: 3115

## Prime Factorization

### Template: Trial Division

Key insight: divide by each candidate d while d*d <= x. If x > 1 after all divisions, x itself is a prime factor.

```py
# find all prime factors
ans = set()
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
```

LC: 2521, 2507, 2584

### Variant: Track Leftmost/Rightmost Occurrences

For problems where you need to know the range of each prime factor (split problems, interval coverage).

```py
left = {}   # first index where prime p appears
right = [0] * len(nums)  # last index where any prime in nums[i] appears

def record_prime(p: int, i: int) -> None:
    if p in left:
        right[left[p]] = i
    else:
        left[p] = i

for i, x in enumerate(nums):
    # factorize x and record each prime
    d = 2
    while d * d <= x:
        if x % d == 0:
            record_prime(d, i)
            while x % d == 0:
                x //= d
        d += 1
    if x > 1:
        record_prime(x, i)
```

LC: 2584

## Large Prime Optimization

Key insight: a number can have at most one prime factor greater than its square root.

For numbers up to 10^9, check divisibility by small primes (up to sqrt(10^9) = 31623), then whatever remains is the large prime.

```py
# find all prime factors less than sqrt(max(nums))
primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}  # all primes <= sqrt(1000)
ans = set()
for p in primes:
    if n%p == 0:
        ans.add(p)
        while n%p == 0:
            n //= p
# find a large prime
if n!=1: ans.add(n)
```

When to use: numbers up to 10^9, need prime factors but can't afford full trial division.

LC: 2521

## Least Prime Factor (LPF) Precomputation

Key insight: for problems requiring prime/factor info on many numbers up to n, precompute LPF for all numbers in O(n log log n).

```py
n = 10**6
LPF = [0] * n
for i in range(2, n):
    if LPF[i] == 0:  # i is prime
        for j in range(i, n, i):
            if LPF[j] == 0:
                LPF[j] = i
```

After precomputation, LPF[x] gives the smallest prime factor of x. Use this to factorize x by repeatedly dividing by LPF[x].

When to use: need prime/factor info for many numbers up to 10^6, want O(1) access after O(n log log n) preprocessing.

LC: 3326

## Sieve of Eratosthenes

Key insight: iteratively mark multiples of each prime as composite. Start marking from i*i (smaller multiples already marked).

The sieve finds all primes up to n in O(n log log n) time.

### Template: Count Primes

```py
def countPrimes(n):
    if n<2: return 0

    sieve = [1]*n
    sieve[0] = sieve[1] = 0
    for i in range(int(sqrt(n))+1):
        if sieve[i]:
            for j in range(i*i, n, i):
                sieve[j] = 0
    return sum(sieve)
```

LC: 204

### Template: Find Primes

```py
def findPrimes(n):
    if n<2: return []

    sieve = [1]*n
    sieve[0] = sieve[1] = 0
    for i in range(int(sqrt(n))+1):
        if sieve[i]:
            for j in range(i*i, n, i):
                sieve[j] = 0
    return [i for i in range(n) if sieve[i]]
```

LC: 2523, 2601

## Prime Factorization + Union Find

Key insight: connect numbers by their prime factors. Union each number with its factors. Numbers in the same component share at least one prime factor.

```py
class DSU:
    def __init__(self, n):
        self.p = [i for i in range(n)]

    def find(self, u):
        if self.p[u] != u:
            self.p[u] = self.find(self.p[u])
        return self.p[u]

    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)

dsu = DSU(max(A) + 1)
for x in A:
    for p in range(2, int(sqrt(x)) + 1):
        if x % p == 0:
            dsu.union(x, p)
            dsu.union(x, x // p)

# count component sizes
cnt = Counter(dsu.find(x) for x in A)
```

When to use: need to group numbers by shared prime factors, query connectivity or component size.

LC: 952, 1998, 2709

## Reference

- [wiki: Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
