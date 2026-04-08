---
tags:
  - leetcode
  - prefixsum
  - moc
---

# Prefix Sum

## When to Use

| Problem Signal | Technique |
|---|---|
| Range sum/product query (static array) | 1D/2D prefix sum |
| Range XOR query | Prefix XOR |
| Batch range updates, then query final state | Difference array (sweep line) |
| Count overlapping intervals / max overlap | Difference array (sweep line) |
| Answer depends on both left and right context | Prefix suffix decomposition |
| Count subarrays with sum = k | Prefix sum + hash table |
| Longest subarray with sum = k | Prefix sum + hash table (store first occurrence) |
| Subarray sum divisible by k | Prefix sum mod k + hash table |
| Subarray with even/odd character counts | Bitmask prefix XOR + hash table |

## 1D Prefix Sum

### Build

```py
# prefix sum (0-indexed, length n+1, prefix[0] = 0)
prefix = list(accumulate(A, initial=0))

# prefix product
prefix = list(accumulate(A, mul, initial=1))
```

### Query

```py
# sum of A[l..r] inclusive
prefix[r + 1] - prefix[l]
```

## 1D Prefix XOR

XOR is its own inverse, so the same prefix pattern works.

```py
prefix = list(accumulate(A, xor, initial=0))

# xor of A[l..r] inclusive
prefix[r + 1] ^ prefix[l]
```

## 2D Prefix Sum

### Build

```py
m, n = len(A), len(A[0])
prefix = [[0] * (n + 1) for _ in range(m + 1)]
for i in range(m):
    for j in range(n):
        prefix[i + 1][j + 1] = A[i][j] + prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j]
```

### Query

```py
# sum of submatrix A[r1..r2][c1..c2] inclusive
prefix[r2 + 1][c2 + 1] - prefix[r2 + 1][c1] - prefix[r1][c2 + 1] + prefix[r1][c1]
```

### Build (bottom-right to top-left)

Useful when you need suffix-style 2D sums.

```py
m, n = len(A), len(A[0])
prefix = [[0] * (n + 1) for _ in range(m + 1)]
for i in reversed(range(1, m + 1)):
    for j in reversed(range(1, n + 1)):
        prefix[i - 1][j - 1] = A[i - 1][j - 1] + prefix[i][j - 1] + prefix[i - 1][j] - prefix[i][j]
```

### 2D to 1D Reduction

For problems like "count submatrices with sum = target" (LC 1074), fix two rows and reduce to a 1D prefix sum + hash table problem.

```py
for r1 in range(m):
    col_sum = [0] * n
    for r2 in range(r1, m):
        for c in range(n):
            col_sum[c] += A[r2][c]
        # now solve 1D "subarray sum = k" on col_sum
```

## Difference Array (Sweep Line)

The inverse of prefix sum. Apply range updates in O(1) each, then reconstruct with a prefix sum pass.

Key insight: `diff[i] += val, diff[j+1] -= val` means "add val to every element in [i, j]".

For all interval-update problems, this should be the first intuition.

### Template 1: Array-based

Use when indices are bounded and small. O(n) space, O(1) per update.

```py
n = len(A)
diff = [0] * (n + 1)
for i, j in intervals:
    diff[i] += 1
    diff[j + 1] -= 1

# reconstruct with prefix sum
for i in range(1, n + 1):
    diff[i] += diff[i - 1]
```

### Template 2: Event-based (sort)

Use when indices are sparse or unbounded. O(k log k) where k = number of events.

```py
events = []
for i, j in intervals:
    events.append((i, 1))
    events.append((j + 1, -1))
events.sort()

cnt = 0
for pos, delta in events:
    cnt += delta
    # process position with current count
```

### 2D Difference Array

Apply range updates on a 2D matrix in O(1) each, then reconstruct with 2D prefix sum.

```py
m, n = len(A), len(A[0])
diff = [[0] * (n + 1) for _ in range(m + 1)]
for r1, c1, r2, c2 in queries:
    diff[r1][c1] += 1
    diff[r1][c2 + 1] -= 1
    diff[r2 + 1][c1] -= 1
    diff[r2 + 1][c2 + 1] += 1

# reconstruct with 2D prefix sum
for i in range(m):
    for j in range(n):
        if i > 0: diff[i][j] += diff[i - 1][j]
        if j > 0: diff[i][j] += diff[i][j - 1]
        if i > 0 and j > 0: diff[i][j] -= diff[i - 1][j - 1]
```

## Prefix Suffix Decomposition

Precompute a value from the left (prefix) and from the right (suffix), then combine them to answer queries at each index.

### Template: Separate arrays

```py
n = len(A)
prefix = list(accumulate(A, func))         # prefix[i] = func(A[0..i])
suffix = list(accumulate(A[::-1], func))    # suffix[i] = func(A[n-1..n-1-i])
suffix.reverse()

# answer at index i uses prefix[i-1] and suffix[i+1]
```

### Template: Single pass (O(1) space)

```py
ans = [1] * len(A)
prefix = suffix = identity  # 1 for product, 0 for sum, -inf for max, etc.
for i in range(1, len(A)):
    prefix = func(prefix, A[i - 1])
    suffix = func(suffix, A[~i + 1])
    ans[i] = combine(ans[i], prefix)
    ans[~i] = combine(ans[~i], suffix)
```

### Common patterns

- **Product except self** (LC 238): prefix product * suffix product
- **Prefix max / suffix min** (LC 915): find partition where max(left) <= min(right)
- **Left score / right score** (LC 1422): prefix count + suffix count

## Prefix Sum + Hash Table

The core idea: if `prefix[j] - prefix[i] = k`, then the subarray `A[i+1..j]` has sum k. Use a hash table to find matching prefix values in O(1).

### Count subarrays with sum = k

LC 560, 930, 974

```py
cnt = Counter([0])
ans = prefix = 0
for x in A:
    prefix += x
    ans += cnt[prefix - k]
    cnt[prefix] += 1
return ans
```

### Longest subarray with sum = k

LC 2106, 523, 525

Store the first occurrence of each prefix value.

```py
first = {0: -1}
ans = prefix = 0
for i, x in enumerate(A):
    prefix += x
    if prefix - k in first:
        ans = max(ans, i - first[prefix - k])
    first.setdefault(prefix, i)
return ans
```

### Modulo variant (divisible by k)

LC 974, 1590

If `prefix[j] % k == prefix[i] % k`, then `sum(A[i+1..j])` is divisible by k.

```py
cnt = Counter([0])
ans = prefix = 0
for x in A:
    prefix = (prefix + x) % k
    ans += cnt[prefix]
    cnt[prefix] += 1
return ans
```

For "shortest/longest subarray to remove so remainder = 0" (LC 1590):

```py
first = {0: -1}
target = sum(A) % p
prefix = 0
ans = inf
for i, x in enumerate(A):
    prefix = (prefix + x) % p
    if (prefix - target) % p in first:
        ans = min(ans, i - first[(prefix - target) % p])
    first[prefix] = i  # store latest occurrence for shortest
```

### Bitmask variant (parity / XOR state tracking)

LC 1371, 1542, 1915

Use XOR to track odd/even counts of characters. Two prefix states that are equal mean the subarray between them has all even counts.

**Longest subarray with all even counts:**

```py
first = {0: -1}
ans = prefix = 0
for i, c in enumerate(s):
    if c in target_chars:
        prefix ^= 1 << char_index(c)
    if prefix in first:
        ans = max(ans, i - first[prefix])
    first.setdefault(prefix, i)
return ans
```

**Count subarrays with at most one odd-count character:**

```py
cnt = Counter([0])
ans = prefix = 0
for c in s:
    prefix ^= 1 << (ord(c) - ord('a'))
    # exact match: all even
    ans += cnt[prefix]
    # one bit difference: exactly one odd
    ans += sum(cnt[prefix ^ (1 << i)] for i in range(num_chars))
    cnt[prefix] += 1
return ans
```
