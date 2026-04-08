---
tags:
  - leetcode
  - greedy
  - moc
---

# Greedy

A greedy algorithm is any algorithm that follows the problem-solving heuristic of making the locally optimal choice at each stage. In many problems, a greedy strategy does not usually produce an optimal solution, but nonetheless, a greedy heuristic may yield locally optimal solutions that approximate a globally optimal solution in a reasonable amount of time.

## When to Use

| Problem Signal | Technique | LeetCode Examples |
|---|---|---|
| **Intervals:** Remove minimum intervals to make non-overlapping | Sort by end, keep earliest finishing | 435, 452 |
| **Intervals:** Merge overlapping intervals | Sort by start, merge when overlap detected | 56, 57 |
| **Intervals:** Maximum non-overlapping intervals | Sort by end, greedily pick earliest finishing | 435, 646 |
| **Optimization:** Minimize/maximize by moving to median | Median minimizes sum of absolute deviations | 462, 296, 2448 |
| **Optimization:** Minimize/maximize weighted median | Weighted median or binary search on answer | 2448, 2607, 1703 |
| **Constraints:** Assign values satisfying local constraints | Two-pass: forward + backward with max | 135 (Candy), 2100 |
| **Counting:** Count contribution of each element across all subarrays | Track prev occurrence, compute contribution range | 907, 2104, 2262, 828 |
| **Rearrangement:** Avoid adjacent duplicates | Fill odd positions first, then even | 767, 1054, 984 |
| **Assignment:** Pair/match elements optimally | Sort both arrays, match greedily | 455, 1029 |
| **Sorting + Greedy:** Order matters for optimal choice | Sort by custom key, greedily select | 1029, 406, 2136 |
| **String Construction:** Build string satisfying constraints | DI-string: pop from min/max stack | 942, 2375 |
| **State Machine:** Match subsequences efficiently | Precompute next char positions per state | 792, 524 |
| **Majority Voting:** Find element appearing > n/k times | Boyer-Moore voting algorithm | 169, 229 |
| **Prefix invariant:** Valid start point exists if total valid | Greedy prefix sum with reset | 134 (Gas Station) |

## IntervalProblem

Sort intervals, then greedily select or merge based on endpoints. Key decision: sort by start or end?

### Template 1: Maximum Non-overlapping Intervals

Sort by end time, greedily pick earliest finishing intervals.

LC 435, 452, 646

```py
def maxNonOverlapping(intervals):
    intervals.sort(key=lambda x: x[1])  # sort by end
    ans = 0
    end = -inf
    for i, j in intervals:
        if end <= i:  # no overlap
            end = j
            ans += 1
    return ans
```

### Template 2: Merge Overlapping Intervals

Sort by start time, merge when overlap detected.

LC 56, 57

```py
def merge(intervals):
    ans = []
    for x, y in sorted(intervals):
        if not ans or ans[-1][1] < x:  # no overlap
            ans.append([x, y])
        else:  # overlap
            ans[-1][1] = max(ans[-1][1], y)
    return ans
```

### Key Insights

- **Sort by end** when you want to maximize count of non-overlapping intervals (earliest finish time heuristic)
- **Sort by start** when you want to merge or process intervals in order
- **Minimum removals** = Total intervals - Maximum non-overlapping

## Median

The median minimizes the sum of absolute deviations. Use when the objective is to minimize total distance/cost to a target value.

### Template: Standard Median Problem

LC 462, 296, 2033

```py
def minMoves(A):
    target = sorted(A)[len(A) // 2]
    return sum(abs(a - target) for a in A)
```

### Weighted Median

When elements have weights/costs, use weighted median or binary search.

LC 2448, 2607

```py
def minCost(A, cost):
    # sort by value with costs
    pairs = sorted(zip(A, cost))

    # find weighted median
    total = sum(cost)
    cumsum = 0
    for val, c in pairs:
        cumsum += c
        if cumsum >= (total + 1) // 2:
            target = val
            break

    return sum(abs(a - target) * c for a, c in zip(A, cost))
```

### Advanced: Sliding Window Median

For "make k consecutive subarrays equal" problems, combine with prefix sum and cycle detection.

LC 1703, 2607, 2968

Key insight: the optimal target for a range is the median of that range.

## TwoPass

Make two passes (forward and backward) to enforce local constraints globally. Common for problems where each element depends on both left and right neighbors.

### Template: Two-pass with Max

LC 135 (Candy), 2100, 821, 1653

```py
def twoPass(A):
    n = len(A)
    ans = [1] * n

    # forward pass: enforce left constraint
    for i in range(1, n):
        if A[i] > A[i - 1]:
            ans[i] = ans[i - 1] + 1

    # backward pass: enforce right constraint
    for i in range(n - 2, -1, -1):
        if A[i] > A[i + 1]:
            ans[i] = max(ans[i], ans[i + 1] + 1)

    return sum(ans)
```

### Key Insights

- Use **max** in second pass to avoid overwriting valid first-pass results
- First pass establishes lower bound, second pass refines
- Common pattern: "satisfy constraint with minimum cost"

## CountSubarrayElement

Instead of enumerating all subarrays, count the contribution of each element to the answer. For each element, determine how many subarrays include it (often as min/max).

### Template: Contribution Counting with Monotonic Stack

LC 907, 2104, 1856

```py
def sumSubarrayMins(A):
    n = len(A)

    # find next smaller on the right
    R = [n] * n
    stk = []
    for i in range(n):
        while stk and A[stk[-1]] > A[i]:
            R[stk.pop()] = i
        stk.append(i)

    # find next smaller on the left
    L = [-1] * n
    stk = []
    for i in range(n - 1, -1, -1):
        while stk and A[stk[-1]] >= A[i]:
            L[stk.pop()] = i
        stk.append(i)

    # for each A[i] as minimum, count subarrays
    ans = 0
    for i in range(n):
        left_count = i - L[i]
        right_count = R[i] - i
        ans += A[i] * left_count * right_count

    return ans % (10**9 + 7)
```

### Template: Character Contribution Tracking

LC 828, 2262

```py
def appealSum(s):
    ans = sm = 0
    last = {}
    for i, c in enumerate(s):
        sm += i - last.get(c, -1)  # contribution of c at position i
        ans += sm
        last[c] = i
    return ans
```

### Key Insights

- **For each element**, compute how many subarrays have it as min/max/unique element
- Use **monotonic stack** to find previous/next smaller/larger in O(n)
- Track **last occurrence** for character counting problems

## Rearrangement

Rearrange elements to satisfy constraints (usually avoiding adjacent duplicates).

### Template: Odd-Even Filling

LC 767, 1054

```py
def reorganizeString(s):
    cnt = Counter(s)
    A = sorted([[v, k] for k, v in cnt.items()], reverse=True)

    # check feasibility
    if A[0][0] > (len(s) + 1) // 2:
        return ""

    ans = [""] * len(s)
    i = 0
    for freq, char in A:
        for _ in range(freq):
            ans[i] = char
            i += 2
            if i >= len(s):
                i = 1  # switch to odd positions

    return "".join(ans)
```

### Key Insights

- Fill **odd positions** (0, 2, 4...) first with highest frequency character
- Then fill **even positions** (1, 3, 5...)
- Feasibility check: max frequency should be at most `(n + 1) // 2`

## Sorting

Sort to enable greedy selection. The sort key is critical to the correctness of the greedy choice.

### Template: Sort by Difference

LC 1029 (Two City Scheduling)

```py
def twoCitySchedCost(costs):
    # sort by difference: who benefits most from going to city A?
    costs.sort(key=lambda x: x[0] - x[1])

    n = len(costs) // 2
    ans = sum(c[0] for c in costs[:n]) + sum(c[1] for c in costs[n:])
    return ans
```

### Template: Sort by Custom Key

LC 406 (Queue Reconstruction), 2136 (Earliest Full Bloom)

```py
# Example: LC 406
def reconstructQueue(people):
    # sort by height descending, then k ascending
    people.sort(key=lambda x: (-x[0], x[1]))

    ans = []
    for p in people:
        ans.insert(p[1], p)  # insert at position k
    return ans
```

### Key Insights

- **Sort by difference** when distributing between two choices
- **Sort descending** then insert when position depends on previous elements
- **Sort by ratio or sum** for optimization problems

## DI-String

Construct permutations satisfying "Decrease" and "Increase" pattern constraints.

### Template: Min/Max Stack

LC 942, 2375

```py
def diStringMatch(s):
    ans, pool = [], list(range(len(s) + 1))
    for c in s:
        if c == "I":
            ans.append(pool.pop(0))  # take smallest
        else:
            ans.append(pool.pop())   # take largest
    ans.append(pool[0])
    return ans
```

### Template: Stack with Reversal

```py
def diStringMatch(s):
    ans, stk = [], []
    for i, c in enumerate(s + "I"):
        stk.append(i)
        if c == "I":
            ans.extend(stk[::-1])
            stk = []
    return ans
```

## StateMachine

Precompute state transitions to efficiently match subsequences or patterns.

### Template: Next Character Position

LC 792, 524

```py
def numMatchingSubseq(s, words):
    n = len(s)
    # states[i][c] = next position of character c from position i
    states = [[-1] * 26 for _ in range(n + 1)]

    # build backward
    for i in range(n - 1, -1, -1):
        for j in range(26):
            states[i][j] = states[i + 1][j]
        states[i][ord(s[i]) - ord('a')] = i + 1

    ans = 0
    for w in words:
        i = 0
        for c in w:
            i = states[i][ord(c) - ord('a')]
            if i == -1:
                break
        else:
            ans += 1

    return ans
```

### Key Insights

- Precompute **next occurrence** of each character from each position
- Time complexity: O(n * 26) preprocessing + O(total word length) query
- Use when matching many subsequences against the same string

## MajorityVoting

Find elements appearing more than n/k times in O(n) time, O(k) space.

### Template: Boyer-Moore (k=2, threshold > n/2)

LC 169

```py
def majorityElement(A):
    cand, freq = None, 0
    for x in A:
        if x == cand:
            freq += 1
        else:
            if freq == 0:
                cand = x
                freq = 1
            else:
                freq -= 1
    return cand
```

### Template: Generalized (threshold > n/k)

LC 229 (k=3, threshold > n/3)

```py
def majorityElement(A):
    cands = {}
    for x in A:
        if x in cands:
            cands[x] += 1
        elif len(cands) < 2:  # k-1 = 2
            cands[x] = 1
        else:
            # decrement all
            cands = {k: v - 1 for k, v in cands.items() if v > 1}

    # verify candidates
    return [k for k in cands if A.count(k) > len(A) // 3]
```

### Key Insights

- At most **k-1** candidates can appear more than n/k times
- Maintain at most k-1 candidates
- When all slots full and new element found, decrement all candidates

## Greedy

General greedy patterns that don't fit other categories.

### Pattern 1: Prefix Sum with Reset

LC 134 (Gas Station)

```py
def canCompleteCircuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1

    tank, start = 0, 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:
            start = i + 1  # reset start point
            tank = 0

    return start
```

**Key insight:** If total gas >= total cost, a solution exists. When prefix sum goes negative, the answer must be after that point.

### Pattern 2: Extend Range Greedily

LC 330 (Patching Array), 45 (Jump Game II)

```py
def minPatches(nums, n):
    miss, ans, i = 1, 0, 0
    while miss <= n:
        if i < len(nums) and nums[i] <= miss:
            miss += nums[i]  # use existing number
            i += 1
        else:
            miss += miss  # patch with miss
            ans += 1
    return ans
```

**Key insight:** If we can form [1, miss-1], adding miss extends range to [1, 2*miss-1].

### Pattern 3: Exchange Argument

LC 2136 (Earliest Full Bloom)

Sort by ending time descending. When should task A come before task B? If swapping them makes the result worse, keep the current order.

```py
def earliestFullBloom(plantTime, growTime):
    # sort by grow time descending
    tasks = sorted(zip(growTime, plantTime), reverse=True)

    ans = plant_end = 0
    for grow, plant in tasks:
        plant_end += plant
        ans = max(ans, plant_end + grow)

    return ans
```

## Common Heuristics

1. **Sorting** is often the first step to enable greedy choices
2. **Two pass** when each element depends on both left and right context
3. **Median** minimizes sum of absolute deviations
4. **Prefix sum with reset** for circular/sequential decision problems
5. **Contribution counting** instead of enumerating subarrays
6. **Exchange argument** to derive optimal ordering

## Proving Greedy Correctness

Common techniques:

1. **Exchange argument:** Show that swapping any two elements makes the solution worse
2. **Induction:** Prove that greedy choice maintains invariant
3. **Stay ahead:** Show greedy solution is always ahead of or equal to optimal
4. **Structural property:** Prove problem has matroid/greedy choice property

## Reference

- [wiki: Greedy algorithm](https://en.wikipedia.org/wiki/Greedy_algorithm)
- [LeetCode 101](https://github.com/changgyhub/leetcode_101)
