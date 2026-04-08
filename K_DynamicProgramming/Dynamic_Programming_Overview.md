---
tags:
  - leetcode
  - dynamicprogramming
  - moc
---

# Dynamic Programming

## When to Use

| Problem Signal | Technique | Subcategory |
|---|---|---|
| Max/min/count ways to partition array/string | Sequential DP | SequentialDP/ |
| Decision at each step depends on limited previous steps | Sequential DP | SequentialDP/ |
| Grid path counting, can only move right/down | Maze DP | Maze/ |
| Grid with obstacles, min cost to reach corner | Maze DP | Maze/ |
| Choose items with weights/values, max value under capacity | 0/1 Knapsack | Knapsack/01-Knapsack/ |
| Unlimited copies of items, max value under capacity | Unbounded Knapsack | Knapsack/UnboundedKnapsack/ |
| Two sequences, find common/different elements | Double Sequence (LCS) | DoubleSequence/ |
| Edit distance, alignment, string matching | Double Sequence | DoubleSequence/ |
| Longest strictly/non-strictly increasing subsequence | LIS | LongestIncreasingSubsequence/ |
| Patience sorting, envelope problem | LIS | LongestIncreasingSubsequence/ |
| Subarray sum optimization (max/min sum) | Kadane's algorithm | Kadane(MaximumSubarray)/ |
| Best time to buy/sell stock | Kadane variant | Kadane(MaximumSubarray)/ |
| Count integers with digit constraints (e.g., no adjacent 1s) | Digit DP | DigitDP/ |
| Count numbers in range with property X | Digit DP | DigitDP/ |
| Merge subarrays [i, j], optimal cost | Interval DP | Interval/ |
| Burst balloons, remove boxes, palindrome partitioning | Interval DP | Interval/ |
| DP on tree structure (subtree optimization) | Tree DP | TreeDP/ |
| Rob houses on tree, max independent set on tree | Tree DP | TreeDP/ |
| Small n (<= 20), assign roles/colors to nodes | Bitmask DP (state compression) | StateCompression/ |
| Traveling salesman, Hamiltonian path | Bitmask DP | StateCompression/ |
| Expected value, game theory, probability of outcome | Probability DP | Probability/ |
| Soup servings, coin toss expected scores | Probability DP | Probability/ |
| Count valid permutations with constraints | Permutation DP | Permutation/ |
| Recurrence like fib(n) = sum(fib(n-i)), n very large (n > 10^6) | Matrix exponentiation | MatrixExponentiationDP/ |
| Linear recurrence + huge n | Matrix exponentiation | MatrixExponentiationDP/ |
| DP with monotonic queue/stack/heap/segment tree | Data structure optimization | DataStructureOptimizedDP/ |
| Sliding window max, range query during DP | Data structure optimization | DataStructureOptimizedDP/ |
| Current state depends on ALL previous states | Dependent DP | DependentDP/ |
| Word break, can partition into dict words | Dependent DP | DependentDP/ |
| Problem requires counting subsequences | Longest Subsequence | LongestSubsequence/ |
| Grid problems not path-counting (paint house, etc.) | Two-dimensional DP | TwoDimensional/ |
| Special/one-off problems | Special | Special/ |

## Problem Solving Steps

1. Split the original question into sub-problems
2. Confirm state definition and dimensions
3. Confirm boundary conditions
4. Find state-transition equation
5. Check if space optimization (rolling array) is possible

## Sequential DP

Current state depends on a fixed number of previous states (e.g., `dp[i]` depends on `dp[i-1]`, `dp[i-2]`).

**Key insight:** Markovian property, limited history matters.

**Template:**

```py
@cache
def dp(i):
    if i < 0: return base_case
    return transition(dp(i-1), dp(i-2), ...)
```

**LC references:** 70 (Climbing Stairs), 198 (House Robber), 1137 (Tribonacci), 2140, 2400

## Maze DP

Grid traversal with constraints (can only move right/down). Often 2D DP with bottom-up fill.

**Key insight:** Path counting or min cost to reach each cell.

**Template:**

```py
# top-down
@cache
def dp(i, j):
    if i == 0 and j == 0: return base
    if i < 0 or j < 0: return inf or 0
    return transition(dp(i-1, j), dp(i, j-1))

# bottom-up
for i in range(m):
    for j in range(n):
        dp[i][j] = transition(dp[i-1][j], dp[i][j-1])
```

**LC references:** 62, 63, 64, 120 (Triangle), 931, 1463 (Cherry Pickup II), 2328

## Knapsack

### 0/1 Knapsack

Each item can be chosen at most once. State: `dp[i][w]` = max value using first i items with capacity w.

**Key insight:** For each item, choose to take it or skip it.

**Template (space-optimized):**

```py
dp = [0] * (capacity + 1)
for weight, value in items:
    for w in range(capacity, weight - 1, -1):
        dp[w] = max(dp[w], dp[w - weight] + value)
```

**LC references:** 416, 494, 1049, 2140, 2400, 2431

### Unbounded Knapsack

Unlimited copies of each item. Same state definition, but can reuse items.

**Key insight:** For each item, decide how many copies to take (or iterate forward in 1D).

**Template (space-optimized):**

```py
dp = [0] * (capacity + 1)
for weight, value in items:
    for w in range(weight, capacity + 1):
        dp[w] = max(dp[w], dp[w - weight] + value)
```

**LC references:** 322, 377, 518, 1155, 2466

## Double Sequence (LCS and variants)

Two sequences s1, s2. State: `dp[i][j]` = answer for s1[:i] and s2[:j].

**Key insight:** At each (i, j), consider if s1[i-1] == s2[j-1].

**Template (Longest Common Subsequence):**

```py
@cache
def dp(i, j):
    if i == 0 or j == 0: return 0
    if s1[i-1] == s2[j-1]:
        return dp(i-1, j-1) + 1
    return max(dp(i-1, j), dp(i, j-1))
```

**LC references:** 72 (Edit Distance), 1035, 1143, 1312, 583

## Longest Increasing Subsequence (LIS)

Find longest strictly increasing subsequence. O(n^2) DP or O(n log n) with binary search + greedy.

**Key insight:** Maintain an array of smallest tail elements for each length.

**Template (O(n log n)):**

```py
from bisect import bisect_left
tails = []
for x in nums:
    pos = bisect_left(tails, x)
    if pos == len(tails):
        tails.append(x)
    else:
        tails[pos] = x
return len(tails)
```

**LC references:** 300, 354, 1187, 1671, 1691, 1964

## Kadane's Algorithm (Maximum Subarray)

Find subarray with maximum sum. Classic 1D DP.

**Key insight:** At each position, decide to extend the current subarray or start fresh.

**Template:**

```py
max_ending_here = max_so_far = -inf
for x in nums:
    max_ending_here = max(x, max_ending_here + x)
    max_so_far = max(max_so_far, max_ending_here)
return max_so_far
```

**Variants:** Max product subarray (152), max absolute sum (1749), stock trading (121, 122, 123).

**LC references:** 53, 121, 152, 918, 1749

## Digit DP

Count integers in range [L, R] satisfying digit constraints. Build number digit by digit, track tight bounds.

**Key insight:** Iterate digits, track if current number is still bounded by L or R.

**Template:**

```py
@cache
def dfs(i, limit_low, limit_high, ...state):
    if i == n: return base_case
    lo = int(low[i]) if limit_low else 0
    hi = int(high[i]) if limit_high else 9
    ans = 0
    for d in range(lo, hi + 1):
        ans += dfs(i+1, limit_low and d==lo, limit_high and d==hi, ...new_state)
    return ans
```

**LC references:** 233, 357, 600, 788, 902, 1067, 1215, 2376

## Interval DP

Merge or partition subarrays [i, j]. State: `dp[i][j]` = optimal answer for subarray [i, j].

**Key insight:** Try all split points k in [i, j) and combine results.

**Template:**

```py
@cache
def dp(i, j):
    if i >= j: return base_case
    ans = inf  # or -inf for max
    for k in range(i, j):
        ans = min(ans, dp(i, k) + dp(k+1, j) + cost(i, j))
    return ans
```

**LC references:** 312 (Burst Balloons), 375, 516, 664, 1000, 1039

## Tree DP

DP on tree structures. State typically: `dp[node][choice]` = answer for subtree rooted at node.

**Key insight:** Recurse on children, aggregate results, decide for current node.

**Template:**

```py
@cache
def dp(node, parent, ...state):
    if is_leaf(node):
        return base_case
    ans = 0
    for child in G[node]:
        if child == parent: continue
        ans += dp(child, node, ...state)
    return ans
```

**LC references:** 337 (House Robber III), 543, 687, 968, 979, 1372, 2925

## State Compression (Bitmask DP)

Small n (<= 20), use bitmask to represent state of n items.

**Key insight:** State space is 2^n, use bit operations to track subsets.

**Template:**

```py
@cache
def dp(mask, ...state):
    if mask == target: return base_case
    ans = inf
    for i in range(n):
        if mask & (1 << i): continue  # already used
        ans = min(ans, cost(i) + dp(mask | (1 << i), ...state))
    return ans
```

**LC references:** 847, 943, 1125, 1723, 1931, 1986, 2172

## Probability DP

Expected value or probability of outcome. State: `dp[...] = probability or expected score`.

**Key insight:** Use probability rules: `P(A) = sum(P(A|B) * P(B))`.

**Template:**

```py
@cache
def dp(state):
    if terminal(state): return outcome
    prob = 0
    for next_state, transition_prob in transitions(state):
        prob += transition_prob * dp(next_state)
    return prob
```

**LC references:** 808, 837, 1230, 1467, 1547

## Permutation DP

Count valid permutations satisfying constraints. State often includes position and last chosen element.

**Key insight:** Build permutation element by element, track what's been used.

**Template:**

```py
@cache
def dp(i, last, mask):
    if i == n: return 1
    ans = 0
    for choice in valid_choices(last, mask):
        ans += dp(i+1, choice, mask | (1 << choice))
    return ans
```

**LC references:** 903, 1359, 1866

## Matrix Exponentiation DP

Linear recurrence with huge n (> 10^6). Represent recurrence as matrix multiplication, use fast exponentiation.

**Key insight:** `f(n) = A * f(n-1)` where A is a transition matrix. Compute A^n in O(k^3 log n) where k = matrix size.

**Template:**

```py
MOD = 10**9 + 7

def mul(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
    return [
        [sum(x * y for x, y in zip(row, col)) % MOD for col in zip(*b)]
        for row in a
    ]

def pow_mul(a: List[List[int]], n: int, f0: List[List[int]]) -> List[List[int]]:
    res = f0
    while n:
        if n & 1:
            res = mul(a, res)
        a = mul(a, a)
        n >>= 1
    return res
```

**LC references:** 70 (large n variant), 509, 1137, 1220, 3337

## Data Structure Optimized DP

DP transition requires range query/update. Use monotonic queue, segment tree, or BIT to optimize from O(n^2) to O(n log n).

**Key insight:** If transition is `dp[i] = max(dp[j] + f(i, j))` for all j in range, and f is monotonic, use a data structure.

**Common patterns:**
- Monotonic deque for sliding window max/min
- Segment tree for range max/min query
- BIT for range sum query
- Heap for top-k tracking

**LC references:** 1696 (Jump Game VI), 2054, 2944, 3335

## Dependent DP

Current state depends on ALL previous states (not just fixed history).

**Key insight:** Often requires iterating all previous positions or caching all valid states.

**Template:**

```py
@cache
def dp(i):
    if i < 0: return base_case
    ans = 0
    for j in range(i):
        if valid_transition(j, i):
            ans += dp(j)
    return ans
```

**LC references:** 139 (Word Break), 140, 1575, 2221

## Longest Subsequence

Count or find subsequences (not necessarily increasing) with certain properties.

**Key insight:** Similar to LIS but condition differs.

**LC references:** 392, 516, 594, 1048, 1964, 2370

## Two-Dimensional DP

Grid problems beyond simple maze (paint house, game on grid, etc.). State has two spatial dimensions.

**Key insight:** Often need to consider multiple choices at each cell.

**LC references:** 221, 256, 265, 542, 647, 1277

## Special

One-off DP problems that don't fit standard categories.

**LC references:** 1048, 2338

## Reference

- [Leetcode DP Practice](https://zhuanlan.zhihu.com/p/84882320)
- [Kadane's algorithm](https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm)
