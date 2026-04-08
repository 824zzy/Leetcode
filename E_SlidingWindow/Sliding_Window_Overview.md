---
tags:
  - leetcode
  - slidingwindow
  - moc
---

# Sliding Window

## When to Use

| Problem Signal | Technique |
|---|---|
| Find max/min/sum of **fixed-size** subarray | Fixed window |
| Longest/shortest substring with **at most** k X | Dynamic window (at most) |
| Count subarrays with **at most** k X | Dynamic window (at most), ans += j-i+1 |
| Longest/shortest substring with **at least** k X | Dynamic window (at least) |
| Count subarrays with **at least** k X | Dynamic window (at least), complement: n*(n+1)/2 - (at most k-1) |
| Count subarrays with **exactly** k X | atMost(k) - atMost(k-1) |
| Longest substring with property (no duplicates, etc.) | Dynamic window, track violation condition |
| Shortest substring covering target (min window) | Dynamic window, shrink when valid |
| Subarray with sum/product/XOR/OR constraint | Dynamic window with state tracking |

## Fixed Window

For problems where the window size k is given upfront. Slide the window by removing the leftmost element and adding the rightmost element.

**Key insight:** Initialize the first k elements, then slide by updating the window state incrementally.

**LC examples:** 643, 438, 567, 1456, 2461, 1343, 2134

### Template 1: Basic fixed window

```py
def fixed_window(A, k):
    sm = sum(A[:k])  # or Counter(A[:k]) for frequency tracking
    ans = sm / k     # or any initial answer based on first window
    for i in range(k, len(A)):
        sm += A[i]
        sm -= A[i - k]
        ans = max(ans, sm / k)  # update answer
    return ans
```

### Template 2: Fixed window with frequency map

Use when checking for anagrams, permutations, or frequency-based constraints.

**LC 438, 567**

```py
def fixed_window_freq(s, p):
    k = len(p)
    target = Counter(p)
    cnt = Counter(s[:k])
    ans = []
    if cnt == target:
        ans.append(0)
    for i in range(k, len(s)):
        cnt[s[i - k]] -= 1
        if cnt[s[i - k]] == 0:
            del cnt[s[i - k]]
        cnt[s[i]] += 1
        if cnt == target:
            ans.append(i - k + 1)
    return ans
```

### Template 3: Fixed window with constraint (distinct elements)

**LC 2461**

```py
def fixed_window_distinct(A, k):
    cnt = Counter()
    sm = 0
    ans = 0
    for i in range(len(A)):
        cnt[A[i]] += 1
        sm += A[i]
        if i >= k:
            cnt[A[i - k]] -= 1
            sm -= A[i - k]
            if cnt[A[i - k]] == 0:
                del cnt[A[i - k]]
        if len(cnt) == k:  # all distinct
            ans = max(ans, sm)
    return ans
```

## Dynamic Window

For problems where the window size is variable. Use two pointers (i, j) where j expands in a for loop and i shrinks in a while loop when a condition is violated.

**Key insight:** The window [i, j] is maintained by a condition. When the condition is violated, shrink from the left.

**Note:** Classic sliding window works best on **non-negative** element arrays. For arbitrary (negative) elements, consider prefix sum + hash table instead.

### Basic template

```py
i = 0
# cnt/state container
for j in range(len(A)):
    # expand: update cnt/state with A[j]
    while/if condition_violated:
        # shrink: update cnt/state, move i
        i += 1
    # update answer
```

## Find Longest or Shortest Substring/Subarray

For problems asking "longest substring without repeating characters" or "shortest subarray with sum >= k".

**Key insight:** Track the violation condition. When valid, update answer and try to shrink.

**LC examples:** 3, 340, 424, 1493, 2024, 2958, 978, 2730

### Template 1: Longest substring with constraint

**LC 3 (no repeating chars), 340 (at most k distinct), 424 (k replacements)**

```py
def longest_substring(A, k):
    cnt = Counter()
    i = 0
    ans = 0
    for j in range(len(A)):
        cnt[A[j]] += 1
        while violation_condition(cnt, k):  # e.g., cnt[A[j]] > 1, len(cnt) > k
            cnt[A[i]] -= 1
            if cnt[A[i]] == 0:
                del cnt[A[i]]
            i += 1
        ans = max(ans, j - i + 1)
    return ans
```

### Template 2: Longest with max frequency

For problems where you can replace minority elements (LC 424, 2024).

**Key insight:** Window is valid if `(window_size - max_freq) <= k`, meaning we can replace at most k elements.

```py
def longest_with_k_replacements(A, k):
    cnt = Counter()
    i = 0
    ans = 0
    for j in range(len(A)):
        cnt[A[j]] += 1
        while (j - i + 1) - max(cnt.values()) > k:
            cnt[A[i]] -= 1
            i += 1
        ans = max(ans, j - i + 1)
    return ans
```

### Template 3: Shortest subarray with sum >= k

**LC 209, 3097**

```py
def shortest_subarray(A, k):
    i = 0
    sm = 0
    ans = inf
    for j in range(len(A)):
        sm += A[j]
        while sm >= k:
            ans = min(ans, j - i + 1)
            sm -= A[i]
            i += 1
    return ans if ans != inf else -1
```

### Template 4: Bitwise OR/AND tracking

For OR/AND constraints, track bit counts across the window.

**LC 3097**

```py
def shortest_or_at_least_k(A, k):
    cnt = [0] * 32
    x = 0
    i = 0
    ans = inf
    for j in range(len(A)):
        for bit in range(32):
            if A[j] & (1 << bit):
                cnt[bit] += 1
                x |= 1 << bit
        while x >= k and i <= j:
            ans = min(ans, j - i + 1)
            for bit in range(32):
                if A[i] & (1 << bit):
                    cnt[bit] -= 1
                    if cnt[bit] == 0:
                        x ^= 1 << bit
            i += 1
    return ans if ans != inf else -1
```

## Count Subarrays with At Most K X

For problems asking "count subarrays with at most k distinct elements" or "at most k odd numbers".

**Key insight:** For every valid window [i, j], all subarrays ending at j starting from [i..j] are valid. That's `j - i + 1` subarrays.

**LC examples:** 2762, 2302, 3835

### Template

```py
def count_at_most(A, k):
    cnt = Counter()  # or other state container
    i = 0
    ans = 0
    for j in range(len(A)):
        cnt[A[j]] += 1
        while violation_condition(cnt, k):  # e.g., len(cnt) > k
            cnt[A[i]] -= 1
            if cnt[A[i]] == 0:
                del cnt[A[i]]
            i += 1
        ans += j - i + 1  # count all subarrays ending at j
    return ans
```

### Example: At most k distinct elements

```py
def at_most_k_distinct(A, k):
    cnt = Counter()
    i = 0
    ans = 0
    for j in range(len(A)):
        cnt[A[j]] += 1
        while len(cnt) > k:
            cnt[A[i]] -= 1
            if cnt[A[i]] == 0:
                del cnt[A[i]]
            i += 1
        ans += j - i + 1
    return ans
```

## Count Subarrays with At Least K X

For problems asking "count subarrays where max element appears at least k times".

**Key insight:** Use the complement. Total subarrays = n*(n+1)/2. Subtract subarrays with **less than** k occurrences.

**LC examples:** 2962, 2537, 3325

### Template

```py
def count_at_least(A, k):
    n = len(A)
    i = 0
    state = initial_state
    ans = 0
    for j in range(len(A)):
        # update state
        while state >= k:  # have enough, shrink
            # update state, move i
            i += 1
        ans += j - i + 1  # count subarrays with < k
    return n * (n + 1) // 2 - ans
```

### Example: Max element appears at least k times

**LC 2962**

```py
def count_max_at_least_k(A, k):
    mx = max(A)
    n = len(A)
    i = 0
    cnt = 0
    ans = 0
    for j in range(len(A)):
        cnt += A[j] == mx
        while cnt == k:  # found k occurrences, shrink
            cnt -= A[i] == mx
            i += 1
        ans += j - i + 1  # count subarrays with < k occurrences
    return n * (n + 1) // 2 - ans
```

### Example: At least k pairs (frequency-based)

**LC 2537**

For problems where "good" means having at least k pairs (elements with freq >= 2).

```py
def count_good_subarrays(A, k):
    cnt = Counter()
    pairs = 0
    i = 0
    ans = 0
    for j in range(len(A)):
        pairs += cnt[A[j]]  # adding A[j] creates cnt[A[j]] new pairs
        cnt[A[j]] += 1
        while pairs >= k:
            cnt[A[i]] -= 1
            pairs -= cnt[A[i]]  # removing A[i] loses cnt[A[i]] pairs
            i += 1
        ans += i  # all subarrays [0..i-1] to j are good
    return ans
```

## Count Subarrays with Exactly K X (Find Difference)

For problems asking "exactly k distinct elements" or "exactly k odd numbers".

**Key insight:** exactly(k) = atMost(k) - atMost(k-1).

**LC examples:** 992, 1248, 930

### Template

```py
def exactly_k(A, k):
    def at_most(A, k):
        cnt = Counter()
        i = 0
        ans = 0
        for j in range(len(A)):
            cnt[A[j]] += 1
            while len(cnt) > k:
                cnt[A[i]] -= 1
                if cnt[A[i]] == 0:
                    del cnt[A[i]]
                i += 1
            ans += j - i + 1
        return ans
    return at_most(A, k) - at_most(A, k - 1)
```

### Example: Exactly k distinct integers

**LC 992**

```py
def subarrays_with_k_distinct(A, k):
    def at_most(A, k):
        cnt = Counter()
        i = 0
        ans = 0
        for j in range(len(A)):
            cnt[A[j]] += 1
            while len(cnt) > k:
                cnt[A[i]] -= 1
                if cnt[A[i]] == 0:
                    del cnt[A[i]]
                i += 1
            ans += j - i + 1
        return ans
    return at_most(A, k) - at_most(A, k - 1)
```

### Example: Exactly k odd numbers

**LC 1248**

```py
def number_of_subarrays(A, k):
    def at_most(A, k):
        i = 0
        ans = 0
        for j in range(len(A)):
            if A[j] % 2:
                k -= 1
            while k < 0:
                if A[i] % 2:
                    k += 1
                i += 1
            ans += j - i + 1
        return ans
    return at_most(A, k) - at_most(A, k - 1)
```

## Choosing the Right Variant

| Problem Type | Formula | Pattern |
|---|---|---|
| Count with **at most** k X | Direct | `ans += j - i + 1` |
| Count with **at least** k X | Complement | `n*(n+1)/2 - at_most(k-1)` |
| Count with **exactly** k X | Difference | `at_most(k) - at_most(k-1)` |
| Longest with constraint | Greedy expand | `ans = max(ans, j - i + 1)` |
| Shortest with constraint | Greedy shrink | `ans = min(ans, j - i + 1)` when valid |

## Common Pitfalls

1. **Negative elements:** Classic sliding window assumes monotonic contribution. For arrays with negatives, use prefix sum + hash table instead.
2. **Off-by-one:** When shrinking, check if you need `while cnt >= k` or `while cnt > k` based on the problem.
3. **Delete from Counter:** Always check `if cnt[x] == 0: del cnt[x]` to avoid counting zero entries as distinct.
4. **At least vs at most:** "At least k" often needs the complement trick. Don't try to directly count "at least" with sliding window.
5. **Exactly k:** Always use `atMost(k) - atMost(k-1)` for "exactly k" problems.
