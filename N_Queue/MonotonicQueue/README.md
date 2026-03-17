# Monotonic Queue

## When to Use

| Problem Signal | Technique |
|---|---|
| Sliding window maximum/minimum | Monotonic deque (LC 239) |
| DP transition queries range max/min over sliding window | DP + monotonic deque (LC 1696, 1425) |
| Shortest subarray with sum >= k (has negative numbers) | Prefix sum + monotonic increasing deque (LC 862) |
| Optimize equation with constraint abs(xi - xj) <= k | Transform + monotonic deque on derived value (LC 1499) |
| Two-ended range queries (track both min and max) | Two monotonic deques (LC 1438) |

## Core Intuition

Monotonic queue (implemented with deque) maintains a sliding window while keeping elements in monotonic order. The key is deciding when to pop from both ends:

- **Pop left (popleft)**: Element is too old (out of window or violates constraint)
- **Pop right (pop)**: Element is obsolete (incoming element is better)

Chinese mnemonic: "年老色衰" (old and faded). "年老" means left element is too old to stay. "色衰" means right element is inferior to the incoming one.

## Comparison: Monotonic Queue vs Monotonic Stack

| | Monotonic Queue | Monotonic Stack |
|---|---|---|
| **Data structure** | Deque (double-ended) | Stack (single-ended) |
| **Pops from** | Both ends | Right end only |
| **Pattern** | Sliding window | Next/previous greater/smaller |
| **Typical use** | Range queries with moving window | Find nearest element satisfying condition |
| **Complexity** | O(n) amortized | O(n) amortized |
| **Example** | LC 239 (sliding window max) | LC 84 (largest rectangle) |

Both use the "obsolete element" principle: if a new element is better and will stay longer, remove the worse one.

## Template 1: Deque (Index-based)

Use when you need to track positions (e.g., window size constraint).

```py
q = deque()  # stores indices, monotonic decreasing by A[i]
ans = []
for i, x in enumerate(A):
    # pop right: remove obsolete elements (新人更优)
    while q and A[q[-1]] <= x:
        q.pop()
    q.append(i)

    # pop left: remove expired elements (太老了)
    while q and i - q[0] >= k:
        q.popleft()

    if i >= k - 1:
        ans.append(A[q[0]])
return ans
```

**When to use**: LC 239, 1696, 1499

## Template 2: Deque (Value-based)

Use when you only care about values, not positions.

```py
dq = deque()  # stores (value, metadata), monotonic by some criterion
for i, x in enumerate(A):
    # pop left: condition depends on problem
    while dq and CONDITION_OLD:
        dq.popleft()

    # pop right: maintain monotonicity
    while dq and CONDITION_OBSOLETE:
        dq.pop()

    dq.append((x, metadata))
    UPDATE_ANS
```

**When to use**: LC 1499 (store derived values), LC 862 (prefix sum)

## Template 3: Heap (Lazy Deletion)

Use when you can't easily maintain deque invariants or need flexible ordering.

```py
pq = []  # min heap or max heap
for i, x in enumerate(A):
    # lazy deletion: remove stale elements
    while pq and CONDITION_EXPIRED:
        heappop(pq)

    heappush(pq, (value, i))

    if i >= k - 1:
        ans.append(pq[0][0])  # or -pq[0][0] for max heap
```

**When to use**: LC 239 (heap variant), LC 1499 (heap variant)

Trade-off: heap is O(n log n) but simpler to code. Deque is O(n) but requires more thought.

## Pattern 1: Sliding Window Max/Min

**Problem**: Find max (or min) in every window of size k.

**Key insight**: Maintain deque of indices in decreasing order (for max). Front of deque is the max. Pop left when out of window. Pop right when new element is larger.

```py
# LC 239
def maxSlidingWindow(A, k):
    q = deque()
    ans = []
    for i, x in enumerate(A):
        # in: maintain monotonic decreasing
        while q and A[q[-1]] <= x:
            q.pop()
        q.append(i)
        # out: remove expired
        while q and i - q[0] >= k:
            q.popleft()
        if i >= k - 1:
            ans.append(A[q[0]])
    return ans
```

**LC refs**: 239, 1438 (two deques for max and min)

## Pattern 2: DP + Monotonic Queue

**Problem**: DP transition involves max/min over a sliding range of previous states.

**Key insight**: If `dp[i] = max(dp[i-k], ..., dp[i-1]) + cost[i]`, use monotonic deque to track the max dp value in the transition window.

**Template**:

```py
# LC 1696
def maxResult(A, k):
    dq = deque([(0, A[0])])  # (index, dp_value)
    for i in range(1, len(A)):
        # out: remove out-of-window states
        while dq and i - dq[0][0] > k:
            dq.popleft()
        # transition: use best previous state
        dp_i = dq[0][1] + A[i]
        # in: maintain monotonic decreasing by dp value
        while dq and dq[-1][1] < dp_i:
            dq.pop()
        dq.append((i, dp_i))
    return dq[-1][1]
```

**LC refs**: 1696, 1425, 2945

## Pattern 3: Prefix Sum + Monotonic Queue

**Problem**: Find shortest/longest subarray with sum >= k, and array has negative numbers (so prefix sum is not monotonic).

**Key insight**: Transform to prefix sum array. Use monotonic increasing deque on prefix values. For each j, find smallest i where `prefix[j] - prefix[i] >= k`.

```py
# LC 862
def shortestSubarray(A, k):
    prefix = list(accumulate(A, initial=0))
    q = deque()
    ans = inf
    for i, s in enumerate(prefix):
        # in: maintain monotonic increasing
        while q and prefix[q[-1]] >= s:
            q.pop()
        q.append(i)
        # out: pop when condition met
        while q and s - prefix[q[0]] >= k:
            ans = min(ans, i - q[0])
            q.popleft()
    return ans if ans != inf else -1
```

**Why monotonic increasing?** Because if `prefix[j] >= prefix[i]` and j < i, then i is useless (j is always better for future queries).

**LC refs**: 862, 918

## Pattern 4: Optimize Equation with Constraint

**Problem**: Maximize `f(i, j)` subject to `abs(xi - xj) <= k`, where `f` can be decomposed into parts depending only on i or j.

**Key insight**: Rewrite `f(i, j) = g(i) + h(j)`. Maintain monotonic deque on g(i) and slide through j.

**Example (LC 1499)**: Maximize `yi + yj + abs(xi - xj)` where `xj - xi <= k` and j > i.

Rewrite as `(yj + xj) + (yi - xi)`. For each j, find i maximizing `yi - xi`.

```py
def findMaxValueOfEquation(points, k):
    dq = deque()  # stores (xi, yi - xi)
    ans = -inf
    for xj, yj in points:
        # out: xi too far from xj
        while dq and xj - dq[0][0] > k:
            dq.popleft()
        if dq:
            ans = max(ans, yj + xj + dq[0][1])
        # in: maintain monotonic decreasing by yi - xi
        while dq and dq[-1][1] < yj - xj:
            dq.pop()
        dq.append((xj, yj - xj))
    return ans
```

**LC refs**: 1499, 2398

## Pattern 5: Two Monotonic Queues

**Problem**: Track both range max and range min in a sliding window.

**Key insight**: Use two deques, one monotonic decreasing (for max), one monotonic increasing (for min).

```py
# LC 1438
def longestSubarray(A, limit):
    mx_q = deque()  # decreasing
    mn_q = deque()  # increasing
    i = 0
    ans = 0
    for j, x in enumerate(A):
        # in: add to both queues
        while mn_q and A[mn_q[-1]] > x:
            mn_q.pop()
        while mx_q and A[mx_q[-1]] < x:
            mx_q.pop()
        mx_q.append(j)
        mn_q.append(j)
        # out: shrink window if constraint violated
        while mx_q and mn_q and A[mx_q[0]] - A[mn_q[0]] > limit:
            if i == mn_q[0]: mn_q.popleft()
            if i == mx_q[0]: mx_q.popleft()
            i += 1
        ans = max(ans, j - i + 1)
    return ans
```

**LC refs**: 1438

## Common Pitfalls

1. **Forgetting to pop left**: Always check if the front element is expired (out of window or violates constraint).
2. **Wrong monotonicity direction**: Decreasing deque for max, increasing for min. Draw a picture if unsure.
3. **Storing value vs index**: If you need to check window size, store indices. If you need the actual value, store both.
4. **Off-by-one in window size**: If window size is k, element at position i should compare with `i - k` (not `i - k + 1`) for expiration.
5. **Popping from wrong end**: Use `popleft()` for expired elements, `pop()` for obsolete elements.

## Time Complexity

All monotonic queue solutions are O(n) amortized because each element is pushed and popped at most once.

Heap solutions are O(n log n) due to heap operations.

## LC Problem List

| # | Difficulty | Pattern | Notes |
|---|---|---|---|
| 239 | M | Sliding window max | Base template |
| 862 | H | Prefix sum + MQ | Shortest subarray sum >= k |
| 918 | M | Prefix sum + MQ | Circular array max sum |
| 1425 | H | DP + MQ | Constrained subsequence sum |
| 1438 | M | Two MQs | Track max and min |
| 1499 | H | Equation optimization | Transform to derived value |
| 1687 | H | DP + MQ | Delivering boxes |
| 1696 | M | DP + MQ | Jump game with transitions |
| 2398 | H | Equation optimization | Robots within budget |
| 2945 | H | DP + MQ | Non-decreasing array length |
