# Combinatorics

## When to Use

| Problem Signal | Technique |
|---|---|
| Count ways to arrange/select items | Permutation/Combination formulas |
| Count unique orderings with duplicates | Multiset permutation (n! / k1!k2!...) |
| Select k items from n without order | C(n, k) = n! / (k!(n-k)!) |
| Select k items from n with order | P(n, k) = n! / (n-k)! |
| Count paths in grid (right/down moves) | C(h+v, h) |
| Stars and bars (distribute identical items) | C(n+k-1, k-1) |
| Count subarrays containing element at index i | (i+1) * (n-i) |
| Count valid digit sequences (permutation ranking) | Combinatorial digit DP |
| Count objects formed from independent choices | Rule of product |
| Count sets satisfying multiple constraints | Inclusion-exclusion |
| Large mod computations with division | Modular inverse (Fermat's little theorem) |
| Build C(n, k) for many queries | Pascal's triangle |

## Core Formulas

### Permutation and Combination

```py
# Combination: choose k from n (order doesn't matter)
C(n, k) = n! / (k! * (n-k)!)

# Python API
math.comb(n, k)

# Permutation: choose k from n (order matters)
P(n, k) = n! / (n-k)!

# Python API
math.perm(n, k)

# Multiset permutation (n items with k1 of type 1, k2 of type 2, ...)
# Example: permutations of "AABBCC"
n! / (k1! * k2! * ... * km!)
```

### Factorial

```py
# Direct computation
math.factorial(n)

# Iterative
def factorial(n):
    ans = 1
    for i in range(1, n + 1):
        ans *= i
    return ans
```

### Stars and Bars

Distributing n identical items into k bins.

```py
# At least 0 items per bin
C(n + k - 1, k - 1)

# At least 1 item per bin
C(n - 1, k - 1)
```

### Grid Paths

Number of paths from (0,0) to (h,v) moving only right and down.

```py
C(h + v, h)  # or equivalently C(h + v, v)
```

## Rule of Product

If there are `n` ways to do one thing and `m` ways to do another, then there are `n * m` ways to do both.

### Pattern: Independent Choices

When you need to count objects formed from independent choices in multiple dimensions.

```py
# LC 3128: Count right triangles
# For each '1', count ways to pick another '1' in same row and column
for i in range(m):
    for j in range(n):
        if grid[i][j] == 1:
            ans += (row_cnt[i] - 1) * (col_cnt[j] - 1)
```

### Pattern: Counting Subarrays

Number of subarrays containing element at index i.

```py
# LC 2063: Count vowels in all substrings
# Each vowel at index i appears in (i+1) * (n-i) subarrays
for i, c in enumerate(s):
    if c in "aeiou":
        ans += (i + 1) * (len(s) - i)
```

## Inclusion-Exclusion Principle

|A ∪ B ∪ C| = |A| + |B| + |C| - |A ∩ B| - |A ∩ C| - |B ∩ C| + |A ∩ B ∩ C|

### Pattern: Counting Multiples

Count integers in [1, n] divisible by at least one of a, b, c.

```py
# LC 2652: Sum of multiples of 3, 5, or 7
def fn(x):
    f = n // x
    return f * (f + 1) // 2 * x

ans = fn(3) + fn(5) + fn(7) - fn(15) - fn(35) - fn(21) + fn(105)
```

**Key insight:** Add single sets, subtract pairwise intersections, add triple intersection.

### General Template

```py
# For sets A1, A2, ..., An
# Count elements in at least one set
ans = 0
for mask in range(1, 1 << n):
    intersection = compute_intersection(mask)
    sign = 1 if bin(mask).count('1') % 2 == 1 else -1
    ans += sign * intersection
```

## Pascal's Triangle

Build all C(n, k) values efficiently for small n.

```py
# Build Pascal's triangle up to row n
pascal = [[1]]
for i in range(1, n + 1):
    row = [1]
    for j in range(1, i):
        row.append(pascal[i-1][j-1] + pascal[i-1][j])
    row.append(1)
    pascal.append(row)

# Access C(n, k)
pascal[n][k]
```

**Space optimization:** If you only need C(n, k) for specific queries, use `math.comb(n, k)` directly.

## Modular Arithmetic with Division

When computing (a / b) % MOD, you can't just divide. Use modular inverse.

### Fermat's Little Theorem

If MOD is prime, then `b^-1 ≡ b^(MOD-2) (mod MOD)`.

```py
MOD = 10**9 + 7

# Compute (a / b) % MOD
def mod_div(a, b):
    return a * pow(b, MOD - 2, MOD) % MOD

# Equivalently
def mod_div(a, b):
    return a * pow(b, -1, MOD) % MOD  # Python 3.8+
```

### Precompute Factorial Inverses

For repeated C(n, k) computations under mod.

```py
MOD = 10**9 + 7
MX = 100001

# Precompute factorials
fac = [1] * MX
for i in range(1, MX):
    fac[i] = fac[i - 1] * i % MOD

# Precompute inverse factorials
inv_fac = [1] * MX
inv_fac[-1] = pow(fac[-1], -1, MOD)
for i in range(MX - 1, 0, -1):
    inv_fac[i - 1] = inv_fac[i] * i % MOD

# Compute C(n, k) % MOD in O(1)
def comb_mod(n, k):
    if k < 0 or k > n:
        return 0
    return fac[n] * inv_fac[k] % MOD * inv_fac[n - k] % MOD
```

**Use case:** LC 2514 (count anagrams), LC 3343 (balanced permutations).

## Multiset Permutation

Count distinct permutations of n items where there are duplicates.

```py
# LC 2514: Count anagrams of each word in a sentence
def count_anagrams(word):
    cnt = Counter(word)
    n = factorial(len(word))
    for c in cnt.values():
        n //= factorial(c)
    return n % MOD
```

**Formula:** n! / (k1! * k2! * ... * km!) where ki is the count of the i-th unique element.

## Combinatorial Digit DP

Count numbers in range [L, R] with specific digit properties (no repeats, sum constraint, etc).

### Pattern: Count Numbers with Unique Digits

LC 2376, LC 1012

```py
def countSpecialNumbers(N):
    # P(n, k) = n! / (n-k)!
    def P(n, k):
        ans = 1
        for i in range(n - k + 1, n + 1):
            ans *= i
        return ans

    L = list(map(int, str(N + 1)))
    ans = 0

    # Count numbers with fewer digits
    for i in range(1, len(L)):
        ans += P(10, i) - P(9, i - 1)  # exclude leading zeros

    # Count numbers with same length (digit DP)
    seen = [0] * 10
    def dfs(i):
        if i == len(L):
            return
        for x in range(10):
            if i == 0 and x == 0:
                continue
            if seen[x]:
                continue
            if x < L[i]:
                # Can place any valid digits after this
                ans += P(9 - i, len(L) - i - 1)
            elif x == L[i]:
                seen[x] = 1
                dfs(i + 1)

    dfs(0)
    return ans
```

**Key insight:** Split into (1) numbers with fewer digits (pure combinatorics), (2) numbers with same digits (digit DP).

## Combinatorial BST Counting

Count ways to build a BST from a permutation.

### Pattern: BST Reordering

LC 1569: Number of ways to reorder array to get same BST.

```py
def numOfWays(A):
    def dfs(A):
        if len(A) <= 2:
            return 1
        l = [x for x in A if x < A[0]]
        r = [x for x in A if x > A[0]]
        # Ways to interleave l and r while preserving order
        ans = comb(len(l) + len(r), len(r))
        return ans * dfs(l) * dfs(r)

    return (dfs(A) - 1) % (10**9 + 7)
```

**Key insight:** Root is fixed. Count ways to interleave left and right subtrees using C(n, k).

## Permutation Ranking (Kth Permutation)

Find the kth lexicographically smallest permutation/sequence.

### Pattern: Grid Path Ranking

LC 1643: Kth smallest instructions (H = right, V = down).

```py
def kthSmallestPath(destination, k):
    v_cnt, h_cnt = destination
    ans = ""
    lower = 0

    for _ in range(v_cnt + h_cnt):
        if h_cnt == 0:
            return ans + "V" * v_cnt

        # Number of paths starting with H
        num_h = comb(v_cnt + h_cnt - 1, h_cnt - 1)

        if lower + num_h >= k:
            ans += "H"
            h_cnt -= 1
        else:
            ans += "V"
            v_cnt -= 1
            lower += num_h

    return ans
```

**Key insight:** At each step, count how many sequences start with the smaller character. If k is within that range, choose it; otherwise, skip it.

## Reference Problems

### Basic Combinations
- LC 401: Binary watch
- LC 1641: Count sorted vowel strings (stars and bars)
- LC 1079: Letter tile possibilities

### Product Rule
- LC 2063: Vowels of all substrings [(i+1) * (n-i)]
- LC 2125: Laser beams in a bank
- LC 3128: Right triangles
- LC 2348: Zero-filled subarrays

### Multiset Permutation
- LC 2514: Count anagrams (n! / k1!k2!...)
- LC 3343: Balanced permutations (knapsack + multiset)

### Inclusion-Exclusion
- LC 2652: Sum multiples (|A∪B∪C|)
- LC 2475: Unequal triplets

### Digit DP + Combinatorics
- LC 1012: Numbers with repeated digits
- LC 2376: Count special integers (unique digits)
- LC 60: Permutation sequence

### Combinatorial DP
- LC 1569: Reorder array to get same BST
- LC 1643: Kth smallest instructions (grid path ranking)

### Modular Inverse
- LC 2514: Count anagrams
- LC 3343: Balanced permutations

### Constraint Distribution
- Distribute candies among children II (bounded sums)

## Key Insights

1. **Count subarrays containing index i:** `(i + 1) * (n - i)`
2. **Grid paths:** Moving h steps right and v steps down = `C(h + v, h)`
3. **Stars and bars:** Distributing n identical items into k bins = `C(n + k - 1, k - 1)`
4. **Multiset permutation:** Divide by product of factorials of duplicate counts
5. **Modular division:** Use Fermat's little theorem: `a / b ≡ a * b^(MOD-2) (mod MOD)`
6. **Inclusion-exclusion:** Add singletons, subtract pairs, add triples, ...
7. **Digit DP split:** Count numbers with fewer digits (combinatorics) + same-length numbers (DP)
8. **BST counting:** Interleave left and right subtrees using `C(|left| + |right|, |right|)`
9. **Permutation ranking:** Greedily pick smallest valid character, update k by skipping smaller sequences
