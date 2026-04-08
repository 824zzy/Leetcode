---
tags:
  - leetcode
  - twopointers
  - moc
---

# Two Pointers

## When to Use

| Problem Signal | Technique |
|---|---|
| Remove/modify elements in-place | Same direction (fast/slow) |
| Merge two sorted arrays/lists | Same direction (two iterators) |
| Partition array by condition (odd/even, pivot) | Same direction (swap-based) |
| Interval list intersections | Same direction (advance by end time) |
| Longest valid substring/subarray (with shrinking) | Same direction (expand right, shrink left) |
| Find pair with target sum (sorted array) | Different direction (converge on target) |
| Maximize/minimize container, area, product | Different direction (greedy pointer movement) |
| Palindrome checks or expansions | Different direction (expand from center) |
| 3Sum, 4Sum, kSum | Reduce to 2Sum with different direction |
| Partition point, next permutation | Different direction (scan and swap) |

## Same Direction (Fast/Slow)

Key insight: one pointer explores, the other maintains a boundary or tracks valid state.

### Pattern 1: In-place modification (swap-based)

Use when you need to partition, deduplicate, or rearrange elements without extra space.

LC 26, 27, 80, 283

```py
i = 0
for j in range(len(A)):
    if CONDITION(A[j]):
        A[i], A[j] = A[j], A[i]
        i += 1
# A[:i] is the valid part
```

**Variants:**
- **Remove element** (LC 27, 283): swap non-target elements to front
- **Remove duplicates** (LC 26, 80): allow at most k occurrences
- **Partition by parity** (LC 905, 922): swap odds/evens to separate regions

### Pattern 2: Merge two sorted sequences

LC 88, 986, 1537

```py
i, j = 0, 0
while i < len(A) and j < len(B):
    if COMPARE(A[i], B[j]):
        USE(A[i])
        i += 1
    else:
        USE(B[j])
        j += 1
# handle remaining elements
```

**Reverse merge** (LC 88): fill from end to avoid overwriting when merging in-place.

```py
m, n = m - 1, n - 1
for k in reversed(range(m + n + 2)):
    if m < 0:
        A[k] = B[n]
        n -= 1
    elif n < 0 or A[m] >= B[n]:
        A[k] = A[m]
        m -= 1
    else:
        A[k] = B[n]
        n -= 1
```

**Interval intersections** (LC 986): advance pointer with earlier end time.

```py
i, j = 0, 0
while i < len(A) and j < len(B):
    l = max(A[i][0], B[j][0])
    r = min(A[i][1], B[j][1])
    if l <= r:
        ans.append([l, r])
    if A[i][1] < B[j][1]:
        i += 1
    else:
        j += 1
```

### Pattern 3: Subsequence matching

LC 392, 524, 1055, 2486, 2825

```py
i = 0
for j in range(len(B)):
    if i < len(A) and MATCH(A[i], B[j]):
        i += 1
# i == len(A) means A is subsequence of B
```

### Pattern 4: Find boundary or split point

Use when you need to find the shortest removal or longest valid range.

LC 1574, 2972

```py
# find rightmost j where A[j:] is sorted
j = n - 1
while j > 0 and A[j - 1] <= A[j]:
    j -= 1

# enumerate i as left endpoint, find j greedily
i = 0
ans = j
while i == 0 or (i < n - 1 and A[i - 1] <= A[i]):
    while j < n and A[i] > A[j]:
        j += 1
    ans = min(ans, j - i - 1)
    i += 1
```

### Pattern 5: Grouping or segmentation

LC 228, 443, 763, 1759, 2109

```py
i = 0
while i < len(A):
    j = i
    while j < len(A) and SAME_GROUP(A[i], A[j]):
        j += 1
    PROCESS_GROUP(A[i:j])
    i = j
```

## Different Direction (Converging)

Key insight: two pointers start at opposite ends and move toward each other, pruning impossible solutions.

### Pattern 1: Two sum on sorted array

LC 167, 633, 1099

```py
l, r = 0, len(A) - 1
while l < r:
    s = A[l] + A[r]
    if s == target:
        return [l, r]
    elif s < target:
        l += 1
    else:
        r -= 1
```

**Variants:**
- **Count pairs** (LC 1099, 1679): accumulate instead of return
- **Two sum closest** (LC 16): track min distance
- **Two sum smaller** (LC 259): count pairs < target

### Pattern 2: Maximize/minimize objective

Use when greedy pointer movement works (monotonic trade-off).

LC 11, 42, 881, 948, 1498

```py
l, r = 0, len(A) - 1
ans = 0
while l < r:
    ans = max(ans, COMPUTE(l, r))
    if SHOULD_MOVE_LEFT(A[l], A[r]):
        l += 1
    else:
        r -= 1
```

**Container with most water** (LC 11): move pointer with smaller height.

```py
while l < r:
    ans = max(ans, (r - l) * min(A[l], A[r]))
    if A[l] < A[r]:
        l += 1
    else:
        r -= 1
```

### Pattern 3: Palindrome check or expansion

LC 5, 647, 680, 2330

**Expand from center** (LC 5, 647): try both odd and even length palindromes.

```py
def expand(l, r):
    while 0 <= l <= r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l + 1 : r]

for i in range(len(s)):
    ans = max(ans, expand(i, i), expand(i, i + 1), key=len)
```

**Palindrome with tolerance** (LC 680, 2330): when mismatch, try deleting one char.

```py
l, r = 0, len(s) - 1
while l < r:
    if s[l] == s[r]:
        l += 1
        r -= 1
    else:
        # try deleting left or right
        return is_palindrome(s[l+1:r+1]) or is_palindrome(s[l:r])
return True
```

### Pattern 4: Partition or rearrangement

LC 31, 75, 189

**Next permutation** (LC 31): find pivot, reverse suffix, swap.

**Dutch flag** (LC 75): three-way partition with mid pointer.

```py
l, mid, r = 0, 0, len(A) - 1
while mid <= r:
    if A[mid] == 0:
        A[l], A[mid] = A[mid], A[l]
        l += 1
        mid += 1
    elif A[mid] == 1:
        mid += 1
    else:
        A[mid], A[r] = A[r], A[mid]
        r -= 1
```

## NSum

Reduce kSum to (k-1)Sum recursively, base case is 2Sum with different direction pointers.

Key insight: sort first, fix outer variables, solve inner 2Sum, skip duplicates.

### 2Sum (sorted array)

LC 167, 633

```py
l, r = 0, len(A) - 1
while l < r:
    s = A[l] + A[r]
    if s == target:
        return [l, r]
    elif s < target:
        l += 1
    else:
        r -= 1
```

### 3Sum

LC 15, 16, 259

```py
A.sort()
ans = []
for i in range(len(A)):
    if i and A[i - 1] == A[i]:
        continue  # skip duplicates
    l, r = i + 1, len(A) - 1
    while l < r:
        s = A[i] + A[l] + A[r]
        if s == target:
            ans.append([A[i], A[l], A[r]])
            l += 1
            while l < r and A[l - 1] == A[l]:
                l += 1
        elif s < target:
            l += 1
        else:
            r -= 1
return ans
```

**Variants:**
- **3Sum closest** (LC 16): track min distance
- **3Sum smaller** (LC 259): when `s < target`, all pairs `(l, l+1..r)` work, add `r - l`
- **Valid triangle** (LC 611): same structure as 3Sum smaller

### 4Sum

LC 18

```py
A.sort()
ans = set()
for i in range(len(A) - 3):
    for j in range(i + 1, len(A) - 2):
        l, r = j + 1, len(A) - 1
        t = target - A[i] - A[j]
        while l < r:
            if A[l] + A[r] == t:
                ans.add((A[i], A[j], A[l], A[r]))
                l, r = l + 1, r - 1
            elif A[l] + A[r] < t:
                l += 1
            else:
                r -= 1
return ans
```

### kSum (general)

Recursively reduce to (k-1)Sum. Base case k=2 uses two pointers.

```py
def kSum(A, target, k):
    if k == 2:
        # two sum with two pointers
        l, r = 0, len(A) - 1
        while l < r:
            s = A[l] + A[r]
            if s == target:
                yield [A[l], A[r]]
                l += 1
            elif s < target:
                l += 1
            else:
                r -= 1
    else:
        for i in range(len(A) - k + 1):
            if i and A[i - 1] == A[i]:
                continue
            for res in kSum(A[i + 1:], target - A[i], k - 1):
                yield [A[i]] + res
```

## Choosing Between Same vs Different Direction

| Criterion | Same Direction | Different Direction |
|---|---|---|
| Array state | Unsorted or sorted | Must be sorted (for pruning) |
| Pointer movement | Independent or sequential | Coordinated (move based on comparison) |
| Goal | Partition, merge, track state | Find pair, optimize objective |
| Typical time | O(n) or O(n log n) | O(n) after sort |
| Space | O(1) (in-place) | O(1) (no extra space) |
| Examples | Remove duplicates, merge arrays | Two sum, container with water |
