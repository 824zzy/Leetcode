# Binary Search

## When to Use

| Problem Signal | Technique |
|---|---|
| Array is sorted, search for target | Classic binary search on sorted array |
| Find first/last occurrence | Binary search with predicate |
| Search in rotated sorted array | Binary search with rotation logic |
| Minimize the maximum / maximize the minimum | Binary search on answer |
| Kth smallest in sorted matrix / multiplication table | Binary search on answer + count |
| Split array to minimize largest sum | Binary search on answer (capacity/threshold) |
| Feasibility check with monotonic property | Binary search on answer |
| Find peak in mountain array | Ternary search or binary search on derivative |
| Longest increasing subsequence (LIS) | Binary search + greedy (patience sorting) |
| Range query on sorted/time-series data | Bisect module |
| Weighted random sampling | Prefix sum + bisect |

## Key Insight

Binary search works on **any monotonic predicate**, not just sorted arrays.

If you can define a boolean function `f(x)` such that:
- `f(x) = False, False, ..., False, True, True, ..., True`

Then binary search finds the first `x` where `f(x) = True` (or last where `f(x) = False`).

This generalizes to "binary search on answer": if larger values make a problem easier to solve (or harder), you can binary search on the answer space.

## Classic Binary Search

### Template 1: Find first position where `A[i] >= target`

Returns insertion point (leftmost valid position). This is `bisect_left` behavior.

```py
def binary_search_left(A: List[int], target: int) -> int:
    l, r = 0, len(A)
    while l < r:
        m = (l + r) // 2
        if A[m] < target:
            l = m + 1
        else:
            r = m
    return l
```

### Template 2: Find last position where `A[i] <= target`

Returns rightmost valid position. This is `bisect_right` behavior minus 1.

```py
def binary_search_right(A: List[int], target: int) -> int:
    l, r = 0, len(A)
    while l < r:
        m = (l + r) // 2
        if A[m] <= target:
            l = m + 1
        else:
            r = m
    return l - 1
```

### Template 3: Generic predicate-based search

Find the first index where `predicate(index)` returns True.

```py
def binary_search_predicate(predicate) -> int:
    l, r = 0, len(A)
    while l < r:
        m = (l + r) // 2
        if predicate(m):
            r = m
        else:
            l = m + 1
    return l
```

**LC References:** 704, 278, 374, 69

### Rotated Sorted Array

When searching in a rotated sorted array, check which half is sorted, then decide which half contains the target.

```py
def search_rotated(A: List[int], target: int) -> int:
    l, r = 0, len(A) - 1
    while l < r:
        m = (l + r) // 2
        # Handle duplicates: A[l] == A[r]
        if A[l] == A[r]:
            l += 1
            continue

        # Check if left half is sorted
        if A[l] <= A[m]:
            if A[l] <= target <= A[m]:
                r = m
            else:
                l = m + 1
        # Right half must be sorted
        else:
            if A[m] < target <= A[r]:
                l = m + 1
            else:
                r = m
    return l if l < len(A) and A[l] == target else -1
```

**LC References:** 33, 81, 153, 154

### Single Element in Sorted Array

Use parity to determine which half to search.

```py
def single_non_duplicate(A: List[int]) -> int:
    l, r = 0, len(A) - 1
    while l < r:
        m = (l + r) // 2
        # Pair m with its partner using XOR
        if A[m] == A[m ^ 1]:
            l = m + 1
        else:
            r = m
    return A[l]
```

**LC References:** 540

## Binary Search on Answer

When the problem asks to "minimize the maximum" or "maximize the minimum", binary search on the answer space instead of the input array.

Key pattern: define a feasibility function `can(x)` that returns True if answer `x` is achievable. If `can` is monotonic, binary search works.

### Template: Minimize the maximum

```py
def minimize_maximum(A: List[int], constraint) -> int:
    def can(x):
        # Check if x is a valid maximum
        # Returns True if we can achieve all constraints with max = x
        pass

    l, r = lower_bound, upper_bound
    while l < r:
        m = (l + r) // 2
        if can(m):
            r = m  # Try smaller maximum
        else:
            l = m + 1
    return l
```

### Common Patterns

**Split array to minimize largest sum** (LC 410, 1011):

```py
def split_array(A: List[int], k: int) -> int:
    def can(max_sum):
        # Can we split into k subarrays with each sum <= max_sum?
        groups = 1
        current_sum = 0
        for x in A:
            if current_sum + x > max_sum:
                groups += 1
                current_sum = x
            else:
                current_sum += x
        return groups <= k

    l, r = max(A), sum(A)
    while l < r:
        m = (l + r) // 2
        if can(m):
            r = m
        else:
            l = m + 1
    return l
```

**Koko eating bananas** (LC 875):

```py
def min_eating_speed(piles: List[int], h: int) -> int:
    def can(k):
        hours = sum((x + k - 1) // k for x in piles)  # Ceiling division
        return hours <= h

    l, r = 1, max(piles)
    while l < r:
        m = (l + r) // 2
        if can(m):
            r = m
        else:
            l = m + 1
    return l
```

**Minimize maximum of array** (LC 2439):

```py
def minimize_array_value(A: List[int]) -> int:
    def can(mx):
        buffer = 0
        for x in A:
            if x < mx:
                buffer += mx - x
            else:
                buffer -= x - mx
            if buffer < 0:
                return False
        return True

    l, r = A[0], max(A) + 1
    while l < r:
        m = (l + r) // 2
        if can(m):
            r = m
        else:
            l = m + 1
    return l
```

**LC References:** 410, 875, 1011, 1482, 2226, 2439, 2513, 2141

### Kth Smallest in Matrix/Table

Binary search on value space + count how many elements are smaller.

```py
def kth_smallest_in_multiplication_table(m: int, n: int, k: int) -> int:
    def count(x):
        # Count how many values <= x in m*n multiplication table
        return sum(min(x // i, n) for i in range(1, m + 1))

    l, r = 1, m * n
    while l < r:
        mid = (l + r) // 2
        if count(mid) < k:
            l = mid + 1
        else:
            r = mid
    return l
```

**LC References:** 378, 668, 719

## Ternary Search

Use ternary search to find the maximum or minimum of a **unimodal function** (single peak or valley).

### Template: Find peak

```py
def ternary_search_max(f, l, r) -> int:
    """Find x in [l, r] that maximizes f(x), where f is unimodal."""
    while l < r:
        m1 = l + (r - l) // 3
        m2 = r - (r - l) // 3
        if f(m1) < f(m2):
            l = m1 + 1
        else:
            r = m2 - 1
    return l
```

### Alternative: Binary search on derivative

For finding a peak in a mountain array, you can use binary search on the slope instead:

```py
def peak_index_in_mountain_array(A: List[int]) -> int:
    l, r = 0, len(A) - 1
    while l < r:
        m = (l + r) // 2
        if A[m] < A[m + 1]:
            l = m + 1
        else:
            r = m
    return l
```

**LC References:** 852, 1095

## Bisect Module

Python's `bisect` module provides efficient implementations of binary search. Always prefer `bisect` over manual implementation when searching in a sorted list.

### API Overview

| Function | Returns | Behavior |
|---|---|---|
| `bisect_left(A, x)` | Leftmost insertion point | First position where `A[i] >= x` |
| `bisect_right(A, x)` | Rightmost insertion point | First position where `A[i] > x` |
| `bisect(A, x)` | Alias for `bisect_right` | Same as `bisect_right` |
| `insort_left(A, x)` | None (modifies A) | Insert x at leftmost valid position |
| `insort_right(A, x)` | None (modifies A) | Insert x at rightmost valid position |
| `insort(A, x)` | None (modifies A) | Alias for `insort_right` |

### Custom Key Function (Python 3.10+)

```py
# Search by custom key
idx = bisect_left(A, target, key=lambda x: x[0])

# Example: time-based key-value store
idx = bisect_right(self.data[key], timestamp, key=lambda x: x[0])
if idx > 0:
    return self.data[key][idx - 1][1]
```

**LC References:** 981

### Common Patterns

**Longest Increasing Subsequence (LIS)** (LC 300, 354):

```py
def length_of_LIS(A: List[int]) -> int:
    tails = []
    for x in A:
        idx = bisect_left(tails, x)
        if idx == len(tails):
            tails.append(x)
        else:
            tails[idx] = x
    return len(tails)
```

**Russian Doll Envelopes** (LC 354):

```py
def max_envelopes(A: List[List[int]]) -> int:
    # Sort by width ascending, height descending
    A.sort(key=lambda x: (x[0], -x[1]))
    # LIS on heights
    tails = []
    for _, h in A:
        idx = bisect_left(tails, h)
        if idx == len(tails):
            tails.append(h)
        else:
            tails[idx] = h
    return len(tails)
```

**Weighted Random Sampling** (LC 528):

```py
def __init__(self, w: List[int]):
    self.prefix = list(accumulate(w))

def pick_index(self) -> int:
    return bisect_left(self.prefix, randint(1, self.prefix[-1]))
```

**Range Queries on Sorted Data** (LC 1712):

```py
# Find valid range for middle subarray
prefix = list(accumulate(A))
for i in range(len(prefix)):
    lower_j = max(bisect_left(prefix, 2 * prefix[i]), i + 1)
    upper_j = min(bisect_right(prefix, 0.5 * (prefix[-1] + prefix[i])), len(prefix) - 1)
    count += max(upper_j - lower_j, 0)
```

**Count elements in range** `[low, high]`:

```py
count = bisect_right(A, high) - bisect_left(A, low)
```

**LC References:** 300, 354, 362, 528, 981, 1712, 2070

## Reference

- [[Python] Powerful Ultimate Binary Search Template. Solved many problems](https://leetcode.com/discuss/study-guide/786126/python-powerful-ultimate-binary-search-template-solved-many-problems)
