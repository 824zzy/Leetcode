---
tags:
  - leetcode
  - math
  - moc
---

# Probability

## When to Use

| Problem Signal | Technique | LC Example |
|---|---|---|
| Random selection from unknown/unbounded stream | Reservoir sampling | 382, 398 |
| Uniform random shuffle | Fisher-Yates shuffle | 384 |
| Generate random number using another RNG | Rejection sampling | 470 |
| Random sampling with non-uniform weights | Prefix sum + binary search | 528 |
| Random point in geometric region (circle, rectangle) | Rejection sampling or polar coordinates | 478, 497 |
| O(1) insert/delete/getRandom with no duplicates | List + hash table (val-to-index map) | 380 |
| O(1) insert/delete/getRandom with duplicates | List + hash table (val-to-indices map) | 381 |
| Random selection without replacement from large space | Virtual index mapping (lazily track used) | 519 |

## Random Library APIs

```py
random.randint(a, b)    # integer from [a, b] inclusive
random.random()         # float from [0.0, 1.0)
random.uniform(a, b)    # float from [a, b] uniform
random.choice(seq)      # pick one element uniformly
random.shuffle(seq)     # in-place shuffle (uses Fisher-Yates internally)
```

## Reservoir Sampling

Uniformly sample k items from a stream of unknown length n. Each item has probability k/n.

**When to use:** Unknown stream length, or O(1) space requirement when array is given but you want to avoid indexing overhead (LC 382, 398).

### Template: Single item (k=1)

```py
cnt, ans = 0, 0
for x in stream:
    cnt += 1
    if random.random() < 1 / cnt:
        ans = x
return ans
```

**Key insight:** The i-th element is chosen with probability 1/i initially, then survives all subsequent elements with probability i/(i+1) * (i+1)/(i+2) * ... * (n-1)/n = i/n. After multiplying by the initial 1/i, final probability is 1/n.

### Template: Multiple items (k>1)

```py
reservoir = []
for i, x in enumerate(stream):
    if i < k:
        reservoir.append(x)
    else:
        j = random.randint(0, i)
        if j < k:
            reservoir[j] = x
return reservoir
```

### Problems

- **LC 382 (Linked List Random Node):** Stream is a linked list, can't index, use reservoir sampling
- **LC 398 (Random Pick Index):** Array given, but reservoir sampling avoids storing all indices for each value

## Fisher-Yates Shuffle

Generate a uniform random permutation of an array in O(n) time and O(1) space.

**When to use:** Need uniform random shuffle (LC 384).

### Template

```py
for i in range(1, len(A)):
    j = randint(0, i)
    A[i], A[j] = A[j], A[i]
```

Or equivalently, swap backwards from the end:

```py
for i in range(len(A) - 1, 0, -1):
    j = randint(0, i)
    A[i], A[j] = A[j], A[i]
```

**Key insight:** At step i, element A[i] is swapped with any of the first i+1 elements (including itself) with probability 1/(i+1). The probability of any element ending up at any position is 1/n.

**Correctness:** There are n! permutations, and each has probability (1/1) * (1/2) * ... * (1/n) = 1/n!.

### Problems

- **LC 384 (Shuffle an Array):** Direct application

## Rejection Sampling

Sample from a target distribution by sampling from an easier distribution and rejecting samples that don't meet criteria.

**When to use:** No closed-form inverse CDF, or sampling from geometric region (LC 470, 478, 497).

### Template

```py
while True:
    sample = SAMPLE_FROM_EASY_DISTRIBUTION()
    if ACCEPT_CONDITION(sample):
        return sample
```

**Key insight:** If you sample uniformly from a superset and reject samples outside the target set, the accepted samples are uniform over the target.

**Efficiency:** Expected number of iterations = area(superset) / area(target). For circle in square, efficiency is π/4 ≈ 78%.

### Problems

- **LC 470 (Implement Rand10 Using Rand7):** Generate rand49 via `(rand7()-1)*7 + rand7()-1`, reject values >= 40, return `rand40 % 10 + 1`
  - Efficiency: 40/49 ≈ 82% acceptance rate
  - Can further optimize by reusing rejected samples

- **LC 478 (Generate Random Point in Circle):** Sample x, y uniformly in bounding square, reject if distance > r
  - Alternative: Use polar coordinates, but must sample radius as `r * sqrt(uniform())` (not `r * uniform()`) to avoid bias toward center

## Weighted Random Sampling

Sample with probability proportional to given weights.

**When to use:** Non-uniform probability distribution (LC 528, 497).

### Template: Prefix sum + binary search

```py
class Solution:
    def __init__(self, w: List[int]):
        self.prefix = list(accumulate(w))

    def pickIndex(self) -> int:
        return bisect_left(self.prefix, randint(1, self.prefix[-1]))
```

**Key insight:** The prefix sum array partitions [1, total] into ranges proportional to weights. A random integer in [1, total] falls into bucket i with probability w[i]/total.

**Time:** O(n) init, O(log n) per query

### Problems

- **LC 528 (Random Pick with Weight):** Direct application
- **LC 497 (Random Point in Non-overlapping Rectangles):** First pick rectangle by area weight, then uniform point within rectangle

## O(1) Insert/Delete/GetRandom

Maintain a set with O(1) insert, delete, and uniform random access.

**When to use:** Need all three operations in O(1) (LC 380, 381).

### Template: No duplicates

```py
class RandomizedSet:
    def __init__(self):
        self.vals = []              # array of values
        self.loc = {}               # val -> index in vals

    def insert(self, val: int) -> bool:
        if val in self.loc:
            return False
        self.loc[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.loc:
            return False
        i = self.loc[val]
        last = self.vals[-1]
        self.vals[i] = last         # overwrite with last element
        self.loc[last] = i          # update last element's index
        self.vals.pop()
        del self.loc[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)
```

**Key insight:** Store values in array for O(1) random access, and maintain a hash table mapping value to index for O(1) lookup. On delete, swap with last element to avoid shifting.

### Template: With duplicates

```py
class RandomizedCollection:
    def __init__(self):
        self.vals = []              # array of values
        self.loc = defaultdict(set) # val -> set of indices

    def insert(self, val: int) -> bool:
        self.loc[val].add(len(self.vals))
        self.vals.append(val)
        return len(self.loc[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.loc[val]:
            return False
        i = self.loc[val].pop()
        last = self.vals[-1]
        self.vals[i] = last
        self.loc[last].add(i)
        self.loc[last].discard(len(self.vals) - 1)
        self.vals.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)
```

**Key insight:** Same as no-duplicates version, but store a set of indices for each value instead of a single index.

### Problems

- **LC 380 (Insert Delete GetRandom O(1)):** No duplicates allowed
- **LC 381 (Insert Delete GetRandom O(1) - Duplicates allowed):** Duplicates allowed

## Virtual Index Mapping

For sampling without replacement from a very large space (e.g., 10^9 elements), maintain a lazy mapping that tracks only the swapped positions.

**When to use:** Large space, small number of samples (LC 519).

### Template

```py
class Solution:
    def __init__(self, m: int, n: int):
        self.total = m * n
        self.map = {}  # track swaps: virtual index -> actual value

    def flip(self) -> List[int]:
        r = random.randint(0, self.total - 1)
        val = self.map.get(r, r)  # get actual value at position r
        self.map[r] = self.map.get(self.total - 1, self.total - 1)
        self.total -= 1
        return [val // self.n, val % self.n]

    def reset(self) -> None:
        self.total = self.m * self.n
        self.map.clear()
```

**Key insight:** Instead of maintaining a full array, use a hash table to track swaps (similar to Fisher-Yates but lazy). Only O(k) space for k flips.

### Problems

- **LC 519 (Random Flip Matrix):** m*n matrix can be 10^8, but only need to track flipped positions

## Polar Coordinates for Geometric Sampling

When sampling points uniformly in a circle, naive `r * uniform()` is wrong because it biases toward center.

**Correct:** `r = R * sqrt(uniform())`, `θ = 2π * uniform()`

**Why:** Area element in polar coordinates is `r dr dθ`. To get uniform area density, need `P(r < x) = x²/R²`, which gives CDF x²/R². Inverse CDF is `R * sqrt(u)` for uniform u.

### Template

```py
rho = radius * sqrt(random.random())
theta = 2 * pi * random.random()
x = x_center + rho * cos(theta)
y = y_center + rho * sin(theta)
```

### Problems

- **LC 478 (Generate Random Point in Circle):** Rejection sampling or polar coordinates

## Reference

- [Reservoir Sampling](https://en.wikipedia.org/wiki/Reservoir_sampling)
- [Fisher-Yates Shuffle](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle)
- [Rejection Sampling](https://en.wikipedia.org/wiki/Rejection_sampling)
- [Inverse Transform Sampling](https://en.wikipedia.org/wiki/Inverse_transform_sampling)
