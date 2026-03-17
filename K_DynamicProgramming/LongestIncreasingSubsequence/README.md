# Longest Increasing Subsequence (LIS)

## When to Use

| Problem Signal | Technique |
|---|---|
| Classic LIS on array | O(n²) DP or O(n log n) binary search |
| LIS with non-strict inequality (≤) | Use `bisect_right` instead of `bisect_left` |
| LIS at each position | Collect answer during binary search (LC 1964) |
| Count number of LIS | O(n²) DP with counter, binary search doesn't work (LC 673) |
| 2D LIS (envelopes, boxes) | Sort by first dim (asc), second dim (desc), run LIS on second (LC 354) |
| Mountain array / bitonic sequence | Prefix LIS + suffix LIS (LC 1671) |
| Transform array with replacements to make increasing | DP with binary search on replacement candidates (LC 1187) |
| Map elements to indices, then LIS | Reduce to LIS on mapped indices (LC 1713) |
| Make k-increasing (split into k chains) | Run LIS on each chain separately (LC 2111) |

## Core Insight

Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

**O(n²) perspective:** `dp[i]` = length of longest increasing subsequence ending at index i.

**O(n log n) perspective (patience sorting):** `dp[i]` = minimum value of the last element in an increasing subsequence of length i+1. This works because we can update with binary search, and a smaller tail value is always better for future extensions.

The O(n log n) algorithm is essentially patience sorting, where we maintain multiple piles (the `dp` array) and place each card on the leftmost pile whose top is ≥ current card.

## Standard LIS

### O(n²) DP

```py
def LIS(A):
    dp = [1] * len(A)
    for i in range(len(A)):
        for j in range(i):
            if A[j] < A[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```

LC 300, 673

### O(n log n) Binary Search + Greedy

```py
def LIS(A):
    dp = []
    for x in A:
        k = bisect_left(dp, x)
        if k == len(dp):
            dp.append(x)
        else:
            dp[k] = x
    return len(dp)
```

LC 300, 354, 1713

**Key insight:** The `dp` array maintains the minimum tail value for each possible LIS length. We use `bisect_left` for strict inequality (<).

### Non-strict Inequality (≤)

Use `bisect_right` instead of `bisect_left`.

```py
def LIS_non_strict(A):
    dp = []
    for x in A:
        k = bisect_right(dp, x)
        if k == len(dp):
            dp.append(x)
        else:
            dp[k] = x
    return len(dp)
```

LC 1964, 2826

## LIS at Each Position

Track the LIS length ending at each position while building the binary search array.

```py
def LIS_at_each_position(A):
    vals = []
    ans = []
    for x in A:
        k = bisect_right(vals, x)  # or bisect_left for strict
        ans.append(k + 1)
        if k == len(vals):
            vals.append(x)
        else:
            vals[k] = x
    return ans
```

LC 1964

## Count Number of LIS

Binary search doesn't work here because we need to track counts. Use O(n²) DP with a counter.

```py
def count_LIS(A):
    dp = [[1, 1] for _ in range(len(A))]  # [length, count]
    for i in range(len(A)):
        cnt = 0
        for j in range(i):
            if A[j] < A[i]:
                if dp[i][0] == dp[j][0] + 1:
                    cnt += dp[j][1]
                elif dp[j][0] + 1 > dp[i][0]:
                    dp[i][0] = dp[j][0] + 1
                    cnt = dp[j][1]
        dp[i][1] = cnt if cnt != 0 else 1
    mx = max(x for x, _ in dp)
    return sum(y for x, y in dp if x == mx)
```

LC 673

## 2D LIS

For 2D objects (envelopes, boxes, cuboids), the key trick is to sort by the first dimension ascending and the second dimension **descending**. This ensures that when we run LIS on the second dimension, we never pick two objects with the same first dimension.

```py
def LIS_2D(A):
    # A is list of [width, height] pairs
    A.sort(key=lambda x: (x[0], -x[1]))

    dp = []
    for _, h in A:
        k = bisect_left(dp, h)
        if k == len(dp):
            dp.append(h)
        else:
            dp[k] = h
    return len(dp)
```

LC 354 (Russian Doll Envelopes), 1691 (Cuboids)

**Why descending on second dimension?** If we have envelopes like `[[1,3], [1,4], [1,5]]`, sorting by width ascending and height ascending would allow us to incorrectly pick all three. Sorting height descending gives `[[1,5], [1,4], [1,3]]`, so we can only pick one (the LIS on heights will be 1).

## Mountain Array (Bitonic)

Compute prefix LIS and suffix LIS separately, then combine. A valid peak at index i requires `prefix[i] > 1` and `suffix[i] > 1`.

```py
def minimum_mountain_removals(A):
    def LIS(A):
        dp = [1] * len(A)
        for i in range(len(A)):
            for j in range(i):
                if A[j] < A[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp

    prefix = LIS(A)
    suffix = LIS(A[::-1])[::-1]
    ans = inf

    for i in range(1, len(A) - 1):
        if prefix[i] > 1 and suffix[i] > 1:
            ans = min(ans, len(A) - (prefix[i] + suffix[i] - 1))
    return ans
```

LC 1671

**Mountain length formula:** `prefix[i] + suffix[i] - 1` (we count the peak twice, so subtract 1).

## LIS with Replacements

Allow replacing elements from a source array to make the sequence strictly increasing. Use DP with binary search on replacement candidates.

```py
def make_array_strictly_increasing(A, B):
    B.sort()

    @cache
    def dp(i, prev):
        if i == len(A):
            return 0
        ans = inf
        # option 1: don't change A[i]
        if A[i] > prev:
            ans = dp(i + 1, A[i])
        # option 2: change A[i] to smallest element in B > prev
        k = bisect_right(B, prev)
        if k < len(B):
            ans = min(ans, 1 + dp(i + 1, B[k]))
        return ans

    ans = dp(0, -inf)
    return ans if ans != inf else -1
```

LC 1187

## Map to Indices, Then LIS

If the problem gives a target sequence and asks for the longest subsequence that matches the target order, map target elements to their indices, then run LIS on those indices.

```py
def minimum_operations_to_make_subsequence(target, A):
    idx = {x: i for i, x in enumerate(target)}
    # filter A to only elements in target, then run LIS on their indices
    mapped = [idx[x] for x in A if x in idx]
    return len(target) - LIS(mapped)
```

LC 1713

## K-Increasing Array

Split the array into k chains (indices i, i+k, i+2k, ...) and run LIS on each chain separately. An array is k-increasing if all k chains are non-decreasing.

```py
def min_operations_k_increasing(A, k):
    def LIS_non_strict(A):
        dp = []
        for x in A:
            k = bisect_right(dp, x)
            if k == len(dp):
                dp.append(x)
            else:
                dp[k] = x
        return len(dp)

    total = 0
    for start in range(k):
        chain = A[start::k]
        total += len(chain) - LIS_non_strict(chain)
    return total
```

LC 2111

**Key insight:** To make a chain non-decreasing, we need `len(chain) - LIS(chain)` replacements (replace everything except the LIS).

## Common Pitfalls

- **bisect_left vs bisect_right:** Use `bisect_left` for strict (<), `bisect_right` for non-strict (≤).
- **2D LIS sorting:** Always sort second dimension descending if first dimension is ascending.
- **Counting LIS:** Binary search doesn't work, must use O(n²) DP with counters.
- **Mountain array:** Need `prefix[i] > 1` AND `suffix[i] > 1` for a valid peak.
- **DP array meaning in O(n log n):** The array doesn't represent an actual subsequence, it's just the minimum tail values for each length.
