---
tags:
  - leetcode
  - dynamicprogramming
  - moc
---

# Longest Subsequence

## When to Use

| Problem Signal | Technique |
|---|---|
| Longest increasing/non-decreasing subsequence | LIS O(n²) DP or O(n log n) binary search |
| Longest arithmetic subsequence (any diff) | O(n²) DP with dict per position |
| Longest arithmetic subsequence (fixed diff) | O(n) hash table sweep |
| Longest subsequence with custom constraint | LIS variant with modified transition |
| Longest common subsequence (LCS) | O(mn) 2D DP |
| Edit distance / Levenshtein distance | O(mn) 2D DP (LCS variant) |
| Shortest common supersequence | Build LCS, then merge remaining chars |
| Russian doll envelopes / 2D sorting | Sort + LIS on second dimension |
| Return actual subsequence (not just length) | Store actual arrays or backtrack |

## Longest Increasing Subsequence (LIS)

### O(n²) DP (bottom-up)

Use when n <= 1000 or when you need to easily extend the transition logic.

```py
dp = [1] * len(A)
for i in range(1, len(A)):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + 1)
return max(dp)
```

### O(n²) DP (top-down)

```py
@cache
def dp(i):
    ans = 1
    for j in range(i):
        if A[j] < A[i]:
            ans = max(ans, 1 + dp(j))
    return ans

return max(dp(i) for i in range(len(A)))
```

### O(n log n) Binary Search

Use when n <= 10^5. Maintains an array `vals` where `vals[i]` is the smallest tail element of all increasing subsequences of length `i+1`.

LC 300, 354, 1964

**Strictly increasing (bisect_left):**

```py
vals = []
for x in A:
    k = bisect_left(vals, x)
    if k == len(vals):
        vals.append(x)
    else:
        vals[k] = x
return len(vals)
```

**Non-decreasing (bisect_right):**

```py
vals = []
ans = []
for x in A:
    k = bisect_right(vals, x)
    ans.append(k + 1)  # length of LIS ending at x
    if k == len(vals):
        vals.append(x)
    else:
        vals[k] = x
return ans  # or len(vals)
```

### LIS with Custom Constraint

Replace the comparison `A[j] < A[i]` with your custom condition.

**Divisible subset** (LC 368): sort first, then `A[i] % A[j] == 0`

**Ideal subsequence** (LC 2370): `abs(A[i] - prev) <= k`, track dp per character

```py
dp = [0] * 26
for x in A:
    char_idx = ord(x) - ord('a')
    mx = max(dp[y] for y in range(max(char_idx - k, 0), min(char_idx + k + 1, 26)))
    dp[char_idx] = mx + 1
return max(dp)
```

### Returning the Actual Subsequence

Store arrays instead of lengths:

```py
dp = [[A[i]] for i in range(len(A))]
for i in range(len(A)):
    for j in range(i):
        if A[i] % A[j] == 0:
            dp[i] = max(dp[i], dp[j] + [A[i]], key=len)
return max(dp, key=len)
```

## Longest Arithmetic Subsequence

### Any Difference (O(n²) with dict)

LC 1027

For each position, track the longest arithmetic subsequence ending at that position for each possible difference.

```py
dp = [defaultdict(lambda: 1) for _ in range(len(A))]
ans = 0
for i in range(1, len(A)):
    for j in range(i):
        diff = A[i] - A[j]
        dp[i][diff] = dp[j][diff] + 1
    ans = max(ans, max(dp[i].values()))
return ans
```

### Fixed Difference (O(n) hash table)

LC 1218

```py
dp = Counter()
for x in A:
    dp[x] = dp[x - diff] + 1
return max(dp.values())
```

## Longest Common Subsequence (LCS)

### Standard LCS

LC 1143, 583, 712

```py
@cache
def dp(i, j):
    if i == len(A) or j == len(B):
        return 0
    if A[i] == B[j]:
        return 1 + dp(i + 1, j + 1)
    return max(dp(i + 1, j), dp(i, j + 1))

return dp(0, 0)
```

Bottom-up 2D DP:

```py
m, n = len(A), len(B)
dp = [[0] * (n + 1) for _ in range(m + 1)]
for i in range(m):
    for j in range(n):
        if A[i] == B[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
return dp[m][n]
```

### Shortest Common Supersequence

LC 1092

Build LCS, then merge both strings by including all characters. When characters match (part of LCS), include once. Otherwise, include from both.

## Edit Distance

LC 72, 583, 712, 1143

Transform string A into string B using insertions, deletions, and substitutions.

```py
@cache
def dp(i, j):
    if i == len(A): return len(B) - j  # insert remaining chars of B
    if j == len(B): return len(A) - i  # delete remaining chars of A
    if A[i] == B[j]:
        return dp(i + 1, j + 1)
    return 1 + min(
        dp(i + 1, j),      # delete A[i]
        dp(i, j + 1),      # insert B[j]
        dp(i + 1, j + 1)   # replace A[i] with B[j]
    )

return dp(0, 0)
```

Bottom-up 2D DP:

```py
m, n = len(A), len(B)
dp = [[0] * (n + 1) for _ in range(m + 1)]
for i in range(m + 1):
    dp[i][0] = i
for j in range(n + 1):
    dp[0][j] = j

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if A[i - 1] == B[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
return dp[m][n]
```

**Variants:**

- **Delete only** (LC 583): `min(dp(i+1, j), dp(i, j+1))` instead of all three ops
- **Cost per operation differs**: use weighted min
- **Minimum ASCII delete sum** (LC 712): track sum instead of count

## Russian Doll Envelopes / 2D Sorting

LC 354

Sort by first dimension ascending, second dimension descending, then run LIS on second dimension. The descending sort on the second dimension ensures that envelopes with the same width don't incorrectly nest.

```py
A.sort(key=lambda x: (x[0], -x[1]))

vals = []
for w, h in A:
    k = bisect_left(vals, h)
    if k == len(vals):
        vals.append(h)
    else:
        vals[k] = h
return len(vals)
```

## Key Insights

1. **LIS binary search intuition**: `vals[i]` stores the smallest tail of all subsequences of length `i+1`. Replacing larger tails with smaller ones keeps future extensions possible.

2. **Strictly vs non-decreasing**: use `bisect_left` for strictly increasing, `bisect_right` for non-decreasing.

3. **LCS to edit distance**: LCS counts matches, edit distance counts mismatches. They're duals. `edit_distance = m + n - 2*LCS` for delete-only operations.

4. **2D sorting trick**: when one dimension must be strictly increasing, sort that dimension ascending and the other descending to prevent ties from incorrectly extending the sequence.

5. **Hash table optimization**: when the transition only depends on a specific previous value (like `x - diff`), replace O(n²) with O(n) using a hash table.

## LeetCode Problems

- **LIS (binary search)**: 300, 354, 1964
- **LIS (custom constraint)**: 368 (divisible), 2370 (ideal), 2713 (matrix)
- **Arithmetic subsequence**: 1027 (any diff), 1218 (fixed diff)
- **LCS**: 1143, 583, 712
- **Edit distance**: 72, 583, 712
- **Shortest common supersequence**: 1092
- **Hash table optimization**: 1218, 2370
