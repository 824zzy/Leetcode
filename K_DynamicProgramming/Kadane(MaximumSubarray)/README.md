# Kadane's Algorithm

## When to Use

| Problem Signal | Technique |
|---|---|
| Maximum/minimum sum of contiguous subarray | Classic Kadane |
| Maximum/minimum sum in circular array | Kadane on both max and min |
| Maximum product of contiguous subarray | Track both max and min product |
| Subarray sum with at most k deletions | k+1 states: dp[deleted_count] |
| Max sum with exactly 1 deletion | Two states: d0 (no deletion), d1 (used deletion) |
| Max variance (max count - min count) | Map to +1/-1 array, run Kadane |
| K-concatenated array max sum | Kadane + categorize by total sum sign |
| Best time to buy/sell stock | Kadane variant tracking min so far |

## Core Idea

Kadane's algorithm finds the maximum sum of a contiguous subarray by looking for all positive contiguous segments and keeping track of the maximum sum among all positive segments.

At each position, the key decision is: **extend the current subarray or start a new one**?

```
dp[i] = max sum of subarray ending at index i
dp[i] = max(A[i], dp[i-1] + A[i])
```

For Kadane variants, it is almost always necessary to consider multiple variables to track different subarray states (e.g., with/without deletion, max/min, left/right).

## Classic Kadane

LC 53, 121, 1749, 978

### Bottom-up (space optimized)

```py
ans, cur = -inf, 0
for x in A:
    cur = max(x, cur + x)
    ans = max(ans, cur)
return ans
```

### Bottom-up (array)

```py
dp = [0] * len(A)
dp[0] = A[0]
for i in range(1, len(A)):
    dp[i] = max(dp[i - 1] + A[i], A[i])
return max(dp)
```

### Top-down

```py
@cache
def dp(i):
    if i == len(A):
        return 0
    return max(dp(i + 1) + A[i], A[i])

return max(dp(i) for i in range(len(A)))
```

## Circular Array

LC 918

When the array wraps around, the maximum sum is either:
1. A normal subarray (use standard Kadane)
2. A subarray that wraps around = total_sum - minimum_subarray

Run Kadane twice: once for max subarray, once for min subarray.

Edge case: if all numbers are negative, return max subarray (don't wrap).

```py
mx = mn = -inf
vx = vn = 0
for x in A:
    vx = max(0, vx) + x
    vn = max(0, vn) - x
    mx = max(mx, vx)
    mn = max(mn, vn)
return mx if mx < 0 else max(mx, sum(A) + mn)
```

## Maximum Product

LC 152

Track both maximum and minimum product, because a negative number can flip them.

```py
ans, maxP, minP = -inf, 1, 1

for x in A:
    maxP, minP = max(x, maxP * x, minP * x), min(x, maxP * x, minP * x)
    ans = max(ans, maxP)
return ans
```

## With Deletion

LC 1186

Maintain two states:
- `d0`: max sum ending here with 0 deletions
- `d1`: max sum ending here with 1 deletion used

```py
ans = d0 = d1 = -inf
for x in arr:
    d0, d1 = max(x, x + d0), max(d0, x + d1)
    ans = max(ans, d0, d1)
return ans
```

Transition logic:
- `d0 = max(x, x + d0)` (start fresh or extend)
- `d1 = max(d0, x + d1)` (delete current element or extend with deletion already used)

## K-Concatenation

LC 1191

Categorize by total sum:
1. If k = 1: standard Kadane
2. If total sum > 0: middle (k-2) copies contribute `total * (k-2)`, plus max prefix and max suffix
3. If total sum ≤ 0: just consider prefix + suffix from first 2 copies

```py
# case 1: k = 1
ans, cur = -inf, 0
for x in A:
    cur = max(x, cur + x)
    ans = max(ans, cur)

# case 2 & 3: k > 1
if k > 1:
    pre = max(accumulate(A, initial=0))
    suf = max(accumulate(A[::-1], initial=0))
    sm = max(sum(A) * (k - 2), 0)
    ans = max(ans, sm + pre + suf)

return max(ans, 0) % MOD
```

## Two-Pass Kadane (Variance)

LC 2272

For string variance problems (max frequency of one char minus another), map to +1/-1 array and use bidirectional Kadane.

Since we need at least one -1 in the subarray, run Kadane from both directions and combine at each -1 position.

```py
def fn(A):
    # left-to-right Kadane
    dp1 = [0] * len(A)
    dp1[0] = A[0]
    for i in range(1, len(A)):
        dp1[i] = max(dp1[i - 1] + A[i], A[i])

    # right-to-left Kadane
    dp2 = [0] * len(A)
    dp2[-1] = A[-1]
    ans = 0
    for i in reversed(range(len(A) - 1)):
        dp2[i] = max(dp2[i + 1] + A[i], A[i])
        if A[i] == -1:
            ans = max(ans, dp1[i] + dp2[i] - A[i])
    return ans

# for each pair (a, b), convert string to +1/-1 array
for a in set(s):
    for b in set(s):
        if a == b: continue
        A = [1 if c == a else -1 if c == b else 0 for c in s]
        A = [x for x in A if x != 0]  # remove zeros
        ans = max(ans, fn(A))
```

## Key Insights

1. **Starting fresh vs extending**: At each element, always consider `max(x, cur + x)` not just `cur + x`.

2. **Multiple states**: For variants (deletion, product, circular), track multiple DP states simultaneously.

3. **Product requires min/max**: Negative numbers flip min/max, so track both.

4. **Circular = total - min**: For circular arrays, the wrap-around case equals total sum minus the minimum subarray sum.

5. **Bidirectional Kadane**: When you need to enforce a constraint at a specific position (e.g., "must include this element"), run Kadane from both directions and combine.

6. **Prefix/suffix decomposition**: For K-concatenation, decompose into prefix (from first copy), middle (repeated copies), suffix (from last copy).

## LeetCode Problems

| # | Title | Difficulty | Pattern |
|---|---|---|---|
| 53 | Maximum Subarray | Easy | Classic |
| 121 | Best Time to Buy and Sell Stock | Easy | Kadane variant |
| 152 | Maximum Product Subarray | Medium | Track min/max |
| 918 | Maximum Sum Circular Subarray | Medium | Circular = total - min |
| 978 | Longest Turbulent Subarray | Medium | State machine |
| 1186 | Maximum Subarray Sum with One Deletion | Medium | Two states (with/without deletion) |
| 1191 | K-Concatenation Maximum Sum | Medium | Categorize by total sum |
| 1749 | Maximum Absolute Sum of Any Subarray | Medium | Run Kadane on both +A and -A |
| 2167 | Minimum Time to Remove All Cars Containing Illegal Goods | Medium | Three-part cost model |
| 2272 | Substring With Largest Variance | Hard | Bidirectional Kadane on +1/-1 |
| 2321 | Maximum Score Of Spliced Array | Hard | Kadane on difference array |
| 2708 | Maximum Strength of a Group | Medium | Product variant with negatives |
| 2786 | Visit Array Positions to Maximize Score | Medium | Parity state tracking |
