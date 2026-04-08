---
tags:
  - leetcode
  - dynamicprogramming
  - moc
---

# Knapsack

## When to Use

| Problem Signal | Technique |
|---|---|
| Each item used at most once + capacity constraint | 0/1 Knapsack |
| Items can be used unlimited times + capacity constraint | Unbounded Knapsack |
| Subset sum / partition into equal subsets | 0/1 Knapsack (boolean variant) |
| Minimum coins to make amount / ways to make change | Unbounded Knapsack |
| Job scheduling with non-overlapping intervals | 0/1 Knapsack + binary search |
| Weighted intervals / tasks with profit | 0/1 Knapsack |
| Capacity is small (≤1000) | Strong hint: knapsack |

## 0/1 Knapsack

Key insight: each item can be used at most once. For each item, decide whether to skip or take it.

### Template 1: Top-down (2D state: index + capacity)

```py
@cache
def dp(i, cap):
    if i == len(A):
        return 0  # base case: no more items
    # skip item i
    ans = dp(i + 1, cap)
    # take item i (if it fits)
    if weight[i] <= cap:
        ans = max(ans, value[i] + dp(i + 1, cap - weight[i]))
    return ans

return dp(0, capacity)
```

LC 416, 474, 1049, 1235

### Template 2: Boolean variant (can we reach target?)

Used for subset sum, partition problems where we just need to check feasibility.

```py
@cache
def dp(i, sm):
    if sm == target:
        return True
    if i == len(A) or sm > target:
        return False
    return dp(i + 1, sm) or dp(i + 1, sm + A[i])

return dp(0, 0)
```

LC 416 (partition equal subset sum), 1049 (minimize difference between two subsets)

### Template 3: Multi-dimensional capacity

For problems with multiple constraints (e.g., m zeros and n ones).

```py
@cache
def dp(i, cap1, cap2):
    if i == len(A):
        return 0
    # skip
    ans = dp(i + 1, cap1, cap2)
    # take
    cost1, cost2 = get_cost(A[i])
    if cap1 >= cost1 and cap2 >= cost2:
        ans = max(ans, 1 + dp(i + 1, cap1 - cost1, cap2 - cost2))
    return ans
```

LC 474 (ones and zeros), 879 (profitable schemes)

### Template 4: Job scheduling with binary search

For non-overlapping intervals, sort by end time and use binary search to find next compatible item.

```py
A = sorted([(start, end, profit) for start, end, profit in jobs])

@cache
def dp(i):
    if i == len(A):
        return 0
    # skip current job
    ans = dp(i + 1)
    # take current job, binary search for next compatible
    j = bisect_left(A, (A[i][1], -inf, -inf))
    ans = max(ans, A[i][2] + dp(j))
    return ans

return dp(0)
```

LC 1235 (maximum profit in job scheduling), 1751 (maximum number of events that can be attended II)

### Space-optimized: 1D array (bottom-up)

When you only need the final answer and not intermediate states. Iterate capacity in reverse to avoid using the same item multiple times.

```py
dp = [0] * (capacity + 1)
for i in range(n):
    for cap in range(capacity, weight[i] - 1, -1):
        dp[cap] = max(dp[cap], dp[cap - weight[i]] + value[i])
return dp[capacity]
```

LC 416 (partition equal subset sum)

### Variants

**Three choices per item:** Some problems allow a third option (e.g., assign to left vs right, buy vs sell vs hold).

```py
@cache
def dp(i, state):
    if i == len(A):
        return base_case(state)
    # skip
    ans = dp(i + 1, state)
    # choice 1
    ans = op(ans, value1 + dp(i + 1, new_state1))
    # choice 2
    ans = op(ans, value2 + dp(i + 1, new_state2))
    return ans
```

LC 956 (tallest billboard: skip, add to left, add to right)

## Unbounded Knapsack

Key insight: each item can be used unlimited times. At each capacity, try taking any item and recurse.

### Template 1: Top-down (1D state: remaining capacity)

```py
@cache
def dp(cap):
    if cap == 0:
        return 0
    if cap < 0:
        return inf  # or -inf for max problems
    return min(1 + dp(cap - cost[i]) for i in range(len(A)) if cap >= cost[i])

ans = dp(capacity)
return ans if ans != inf else -1
```

LC 322 (coin change), 983 (minimum cost for tickets)

### Template 2: Count combinations (order matters)

When order matters (e.g., [1,2] and [2,1] are different), try all items at each state.

```py
@cache
def dp(target):
    if target == 0:
        return 1
    return sum(dp(target - x) for x in A if target >= x)

return dp(target)
```

LC 377 (combination sum IV), 2466 (count ways to build good strings)

### Template 3: Count combinations (order doesn't matter)

When order doesn't matter (e.g., [1,2] and [2,1] are the same), track current item index to avoid duplicates.

```py
@cache
def dp(i, target):
    if target == 0:
        return 1
    if target < 0 or i == len(A):
        return 0
    # don't take item i (move to next)
    ans = dp(i + 1, target)
    # take item i (stay at i, since unlimited)
    ans += dp(i, target - A[i])
    return ans

return dp(0, target)
```

Or iterate from current index to avoid sorting:

```py
@cache
def dp(i, target):
    if target == 0:
        return 1
    return sum(dp(j, target - A[j]) for j in range(i, len(A)) if target >= A[j])
```

LC 518 (coin change 2)

### Template 4: With item index (2D state)

Some problems require tracking both item index and remaining capacity.

```py
@cache
def dp(i, cap):
    if cap == 0:
        return 0
    if cap < 0 or i == len(A):
        return inf
    # skip item i (move to next)
    ans = dp(i + 1, cap)
    # take item i (stay at i, since unlimited)
    ans = min(ans, 1 + dp(i, cap - cost[i]))
    return ans
```

LC 322 (coin change - alternative formulation)

### Space-optimized: 1D array (bottom-up)

Iterate capacity forward (unlike 0/1 knapsack) since we want to reuse items.

```py
dp = [inf] * (capacity + 1)
dp[0] = 0
for cap in range(1, capacity + 1):
    for i in range(len(A)):
        if cap >= cost[i]:
            dp[cap] = min(dp[cap], dp[cap - cost[i]] + 1)
return dp[capacity]
```

LC 322 (coin change)

### Variants

**State representation with Counter:** For problems with string/character constraints, use Counter to represent state.

```py
@cache
def dp(state):
    if is_goal(state):
        return 0
    ans = inf
    for item in items:
        new_state = apply_item(state, item)
        ans = min(ans, 1 + dp(new_state))
    return ans
```

LC 691 (stickers to spell word)

**With binary search:** For problems where items have time windows or intervals.

```py
@cache
def dp(i):
    if i >= len(days):
        return 0
    ans = inf
    for duration, cost in tickets:
        j = bisect_right(days, days[i] + duration - 1)
        ans = min(ans, cost + dp(j))
    return ans
```

LC 983 (minimum cost for tickets)

## 0/1 vs Unbounded: How to Choose

| Constraint | Technique |
|---|---|
| "Each item used at most once" / "without replacement" | 0/1 Knapsack |
| "Each item used unlimited times" / "with replacement" | Unbounded Knapsack |
| "Select k items" / "non-overlapping intervals" | 0/1 Knapsack |
| "Minimum coins to make amount" / "ways to make change" | Unbounded Knapsack |
| Capacity ≤ 1000 (small) | Strong hint: knapsack |
| Need to iterate capacity in reverse (1D array) | 0/1 Knapsack |
| Need to iterate capacity forward (1D array) | Unbounded Knapsack |
