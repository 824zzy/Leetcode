---
tags:
  - leetcode
  - advanced
  - moc
---

# Segment Tree

## When to Use

| Problem Signal | Technique | LC Problems |
|---|---|---|
| Point update + range query (sum/max/min) | Basic segment tree (ZKW/tree-based) | 307, 315, 1649 |
| Range update + range query (lazy needed) | Lazy propagation | 715, 729-732, 699, 2569, 2916 |
| Need to track max overlap / booking intervals | Range add max + global max query | 732, 731, 729 |
| Need to set entire range to value + query | Range set sum/max + query | 715, 699 |
| Coordinate compression needed (sparse index) | Tree-based with discretization | 315, 327, 493, 2736 |
| DP on values + range max query | Segment tree as DP table | 2407, 300 |
| Count inversions / smaller elements | Segment tree on sorted values | 315, 493, 327, 1649 |

## Implementation Variants

### When to Pick Which

**ZKW Segment Tree** (array-based, bottom-up):
- Fastest for simple queries (sum/max/min)
- No recursion overhead
- Fixed index range known in advance
- No lazy propagation needed
- Use for: LC 307, 2407

**Tree-based Segment Tree** (dynamic, top-down):
- Supports sparse/unbounded indices (coordinate compression)
- Supports lazy propagation naturally
- Can build nodes on the fly (dynamic growing)
- Use for: LC 315, 327, 715, 729-732, 699, 2213

**Array-based Segment Tree** (1-indexed, recursive):
- Classical implementation, supports lazy propagation
- Fixed index range, 4n space
- Use for: teaching/reference, most problems

## Basic Segment Tree

Point update + range query. No lazy propagation needed.

Key insight: Store aggregate (sum/max/min) at each node covering [l, r]. Query by merging O(log n) disjoint segments.

### ZKW Segment Tree (Fastest for Simple Queries)

LC: 307, 2407

Bottom-up, array-based, no recursion. Leaves start at index n.

```py
class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.T = [0] * 2 * self.n

    def _build(self, A):
        for i in range(self.n):
            self.T[i + self.n] = A[i]
        for i in reversed(range(self.n)):
            self.T[i] = self.T[2 * i] + self.T[2 * i + 1]

    def _set(self, i, val):
        # update single point, propagate to root
        i += self.n
        diff = val - self.T[i]
        while i:
            self.T[i] += diff
            i //= 2

    def _add(self, i, val):
        # add val to single point, propagate to root
        i += self.n
        while i:
            self.T[i] += val
            i //= 2

    def rangeSum(self, l, r):
        ans = 0
        l, r = l + self.n, r + self.n
        while l <= r:
            if l % 2:
                ans, l = ans + self.T[l], l + 1  # if l is right child
            if not r % 2:
                ans, r = ans + self.T[r], r - 1  # if r is left child
            l, r = l // 2, r // 2
        return ans

    def rangeMax(self, l, r):
        ans = 0
        l, r = l + self.n, r + self.n
        while l <= r:
            if l % 2:
                ans, l = max(ans, self.T[l]), l + 1
            if not r % 2:
                ans, r = max(ans, self.T[r]), r - 1
            l, r = l // 2, r // 2
        return ans
```

### Tree-based Segment Tree (Dynamic Growing)

LC: 315, 327, 493, 2736

Supports sparse/unbounded indices. Nodes created on the fly. Useful with coordinate compression.

```py
# Discretization from value to index if necessary
v2i = {x: i for i, x in enumerate(sorted(set(A)))}

class Node:
    def __init__(self, lo, hi, sm=0, mx=0, lazy=None):
        self.lo = lo
        self.hi = hi
        self.sm = sm  # range sum from low to high
        self.mx = mx  # range max from low to high
        self.lazy = lazy  # lazy propagation for range update
        self.left = None
        self.right = None

class SegmentTree:
    def __init__(self, lo, hi, A=[]):
        if A:
            self.root = self._build(lo, hi, A)
        else:
            self.root = Node(lo, hi)

    def _build(self, lo, hi, A):
        # build segment tree based on array A
        node = Node(lo, hi)
        if lo == hi:
            node.sm = A[lo]
            node.mx = A[lo]
        else:
            m = (lo + hi) // 2
            node.left = self._build(lo, m, A)
            node.right = self._build(m + 1, hi, A)
            node.sm = node.left.sm + node.right.sm
            node.mx = max(node.left.mx, node.right.mx)
        return node

    def _add(self, node, i, val):
        # add val to the i-th element
        if node.lo == node.hi:
            node.sm += val
            node.mx += val
            return
        m = (node.lo + node.hi) // 2
        # dynamic growing without building tree
        if not node.left and not node.right:
            node.left = Node(node.lo, m)
            node.right = Node(m + 1, node.hi)

        if i <= m:
            self._add(node.left, i, val)
        elif i > m:
            self._add(node.right, i, val)
        node.sm = node.left.sm + node.right.sm
        node.mx = max(node.left.mx, node.right.mx)

    def _set(self, node, i, val):
        # set the i-th element to val
        if node.lo == node.hi:
            node.sm = val
            node.mx = val
            return
        m = (node.lo + node.hi) // 2
        # dynamic growing without building tree
        if not node.left and not node.right:
            node.left = Node(node.lo, m)
            node.right = Node(m + 1, node.hi)

        if i <= m:
            self._set(node.left, i, val)
        elif i > m:
            self._set(node.right, i, val)
        node.sm = node.left.sm + node.right.sm
        node.mx = max(node.left.mx, node.right.mx)

    def _sumQuery(self, node, lo, hi):
        # return the sum from lo to hi
        if not node:
            return 0
        if node.lo == lo and node.hi == hi:
            return node.sm
        m = (node.lo + node.hi) // 2
        if hi <= m:
            return self._sumQuery(node.left, lo, hi)
        elif lo > m:
            return self._sumQuery(node.right, lo, hi)
        else:
            return self._sumQuery(node.left, lo, m) + self._sumQuery(node.right, m + 1, hi)

    def _maxQuery(self, node, lo, hi):
        # return the max from lo to hi
        if not node:
            return 0
        if node.lo == lo and node.hi == hi:
            return node.mx
        m = (node.lo + node.hi) // 2
        if hi <= m:
            return self._maxQuery(node.left, lo, hi)
        elif lo > m:
            return self._maxQuery(node.right, lo, hi)
        else:
            return max(self._maxQuery(node.left, lo, m), self._maxQuery(node.right, m + 1, hi))
```

### Array-based Segment Tree (1-indexed)

Classical implementation. 1-indexed (o=1 is root, leaves are n to 2n-1).

```py
n = len(nums)
T = [0] * (4 * n)
todo = [0] * (4 * n)

def build(o, l, r):
    # o=1, l=1, r=n for initial call
    if l == r:
        T[o] = nums[l - 1]
        return
    m = (l + r) // 2
    build(o * 2, l, m)
    build(o * 2 + 1, m + 1, r)
    maintain(o)

def maintain(o):
    # sum
    T[o] = T[o * 2] + T[o * 2 + 1]
    # max
    T[o] = max(T[o * 2], T[o * 2 + 1])

def query(o, l, r, L, R):
    # query range [L, R] from segment [l, r] at node o
    if L <= l and r <= R:
        return T[o]
    m = (l + r) // 2
    ans = 0  # or -inf for max
    if m >= L:
        ans += query(o * 2, l, m, L, R)  # sum
        ans = max(ans, query(o * 2, l, m, L, R))  # max
    if m < R:
        ans += query(o * 2 + 1, m + 1, r, L, R)  # sum
        ans = max(ans, query(o * 2 + 1, m + 1, r, L, R))  # max
    return ans

build(1, 1, n)
query(1, 1, n, l + 1, r + 1)
```

## Lazy Propagation

Range update + range query. Push updates lazily to children only when needed.

Key insight: Store pending updates in `lazy` tag. Push down when visiting a node, pull up when returning.

### Range Add + Sum Query

LC: 2569

Add a value to all elements in [lo, hi], then query sum.

```py
class Node:
    def __init__(self, lo, hi, sm=0, lazy=0):
        self.lo = lo
        self.hi = hi
        self.sm = sm
        self.lazy = lazy  # pending add value
        self.left = None
        self.right = None

class SegmentTree:
    def __init__(self, lo, hi):
        self.root = Node(lo, hi)

    def rangeAddSum(self, node, val, lo, hi):
        # add val to the range from lo to hi
        if node.lo == lo and node.hi == hi:
            node.sm += val * (node.hi - node.lo + 1)
            node.lazy += val
            return

        m = (node.lo + node.hi) // 2
        # push lazy to children, if no children, create them
        if not node.left and not node.right:
            node.left = Node(node.lo, m, node.lazy * (m - node.lo + 1), node.lazy)
            node.right = Node(m + 1, node.hi, node.lazy * (node.hi - m), node.lazy)
        else:
            node.left.sm += node.lazy * (m - node.lo + 1)
            node.left.lazy += node.lazy
            node.right.sm += node.lazy * (node.hi - m)
            node.right.lazy += node.lazy
        node.lazy = 0
        # update the children
        if m >= hi:
            self.rangeAddSum(node.left, val, lo, hi)
        elif m < lo:
            self.rangeAddSum(node.right, val, lo, hi)
        else:
            self.rangeAddSum(node.left, val, lo, m)
            self.rangeAddSum(node.right, val, m + 1, hi)
        # update the node
        node.sm = node.left.sm + node.right.sm
        return

    def rangeAddSumQuery(self, node, lo, hi):
        if not node:
            return 0
        if node.lo == lo and node.hi == hi:
            return node.sm
        m = (node.lo + node.hi) // 2
        if hi <= m:
            return node.lazy * (hi - lo + 1) + self.rangeAddSumQuery(node.left, lo, hi)
        elif lo > m:
            return node.lazy * (hi - lo + 1) + self.rangeAddSumQuery(node.right, lo, hi)
        else:
            return node.lazy * (hi - lo + 1) + self.rangeAddSumQuery(node.left, lo, m) + self.rangeAddSumQuery(node.right, m + 1, hi)
```

### Range Add + Max Query

LC: 732, 731, 729

Add a value to all elements in [lo, hi], then query max. Common for calendar/booking problems where you track max overlap.

```py
class Node:
    def __init__(self, lo, hi, mx=0, lazy=0):
        self.lo = lo
        self.hi = hi
        self.mx = mx
        self.lazy = lazy
        self.left = None
        self.right = None

class SegmentTree:
    def __init__(self, lo, hi):
        self.root = Node(lo, hi)

    def rangeAddMax(self, node, val, lo, hi):
        if node.lo == lo and node.hi == hi:
            node.mx += val
            node.lazy += val
            return

        m = (node.lo + node.hi) // 2
        # push lazy to children, if no children, create them
        if not node.left and not node.right:
            node.left = Node(node.lo, m, node.lazy, node.lazy)
            node.right = Node(m + 1, node.hi, node.lazy, node.lazy)
        else:
            node.left.mx += node.lazy
            node.left.lazy += node.lazy
            node.right.mx += node.lazy
            node.right.lazy += node.lazy
        node.lazy = 0
        # update the children
        if m >= hi:
            self.rangeAddMax(node.left, val, lo, hi)
        elif m < lo:
            self.rangeAddMax(node.right, val, lo, hi)
        else:
            self.rangeAddMax(node.left, val, lo, m)
            self.rangeAddMax(node.right, val, m + 1, hi)
        # update the node
        node.mx = max(node.left.mx, node.right.mx)
        return

    def rangeAddMaxQuery(self, node, lo, hi):
        if not node:
            return 0
        if node.lo == lo and node.hi == hi:
            return node.mx
        m = (node.lo + node.hi) // 2
        if hi <= m:
            return node.lazy + self.rangeAddMaxQuery(node.left, lo, hi)
        elif lo > m:
            return node.lazy + self.rangeAddMaxQuery(node.right, lo, hi)
        else:
            return node.lazy + max(self.rangeAddMaxQuery(node.left, lo, m), self.rangeAddMaxQuery(node.right, m + 1, hi))
```

### Range Set + Sum Query

LC: 715

Set all elements in [lo, hi] to a value, then query sum. Use `lazy = None` to distinguish "no pending update" from "set to 0".

```py
class Node:
    def __init__(self, lo, hi, sm=0, lazy=None):
        self.lo = lo
        self.hi = hi
        self.sm = sm
        self.lazy = lazy  # None = no pending update, val = set to val
        self.left = None
        self.right = None

class SegmentTree:
    def __init__(self, lo, hi):
        self.root = Node(lo, hi)

    def rangeSetSum(self, node, val, lo, hi):
        if node.lo == lo and node.hi == hi:
            node.sm = val * (node.hi - node.lo + 1)
            node.lazy = val
            return

        m = (node.lo + node.hi) // 2
        # push lazy to children, if no children, create them on the fly
        if not node.left and not node.right:
            if node.lazy is not None:
                node.left = Node(node.lo, m, node.lazy * (m - node.lo + 1), node.lazy)
                node.right = Node(m + 1, node.hi, node.lazy * (node.hi - m), node.lazy)
            else:
                node.left = Node(node.lo, m)
                node.right = Node(m + 1, node.hi)
        elif node.lazy is not None:
            node.left.sm = node.lazy * (m - node.lo + 1)
            node.left.lazy = node.lazy
            node.right.sm = node.lazy * (node.hi - m)
            node.right.lazy = node.lazy
        # reset lazy tag
        node.lazy = None
        # update the children
        if m >= hi:
            self.rangeSetSum(node.left, val, lo, hi)
        elif m < lo:
            self.rangeSetSum(node.right, val, lo, hi)
        else:
            self.rangeSetSum(node.left, val, lo, m)
            self.rangeSetSum(node.right, val, m + 1, hi)
        # update the node
        node.sm = node.left.sm + node.right.sm
        return

    def rangeSetSumQuery(self, node, lo, hi):
        if not node:
            return 0
        if node.lo == lo and node.hi == hi:
            return node.sm
        m = (node.lo + node.hi) // 2
        if node.lazy is not None:
            return node.lazy * (hi - lo + 1)
        if hi <= m:
            return self.rangeSetSumQuery(node.left, lo, hi)
        elif lo > m:
            return self.rangeSetSumQuery(node.right, lo, hi)
        else:
            return self.rangeSetSumQuery(node.left, lo, m) + self.rangeSetSumQuery(node.right, m + 1, hi)
```

### Range Set + Max Query

LC: 699

Set all elements in [lo, hi] to a value, then query max.

```py
class Node:
    def __init__(self, lo, hi, mx=0, lazy=None):
        self.lo = lo
        self.hi = hi
        self.mx = mx
        self.lazy = lazy
        self.left = None
        self.right = None

class SegmentTree:
    def __init__(self, lo, hi):
        self.root = Node(lo, hi)

    def rangeSetMax(self, node, val, lo, hi):
        if node.lo == lo and node.hi == hi:
            node.mx = val
            node.lazy = val
            return

        m = (node.lo + node.hi) // 2
        # push lazy to children, if no children, create them on the fly
        if not node.left and not node.right:
            node.left = Node(node.lo, m, 0 if node.lazy is None else node.lazy, node.lazy)
            node.right = Node(m + 1, node.hi, 0 if node.lazy is None else node.lazy, node.lazy)
        elif node.lazy is not None:
            node.left.mx = node.lazy
            node.left.lazy = node.lazy
            node.right.mx = node.lazy
            node.right.lazy = node.lazy
        # reset lazy tag
        node.lazy = None
        # update the children
        if m >= hi:
            self.rangeSetMax(node.left, val, lo, hi)
        elif m < lo:
            self.rangeSetMax(node.right, val, lo, hi)
        else:
            self.rangeSetMax(node.left, val, lo, m)
            self.rangeSetMax(node.right, val, m + 1, hi)
        # update the node
        node.mx = max(node.left.mx, node.right.mx)
        return

    def rangeSetMaxQuery(self, node, lo, hi):
        if not node:
            return 0
        if node.lo == lo and node.hi == hi:
            return node.mx
        m = (node.lo + node.hi) // 2
        if node.lazy is not None:
            return node.lazy
        if hi <= m:
            return self.rangeSetMaxQuery(node.left, lo, hi)
        elif lo > m:
            return self.rangeSetMaxQuery(node.right, lo, hi)
        else:
            return max(self.rangeSetMaxQuery(node.left, lo, m), self.rangeSetMaxQuery(node.right, m + 1, hi))
```

### Array-based with Lazy Propagation

General pattern combining query and update with lazy tag.

```py
n = len(nums)
T = [0] * (4 * n)
todo = [0] * (4 * n)

def build(o, l, r):
    if l == r:
        T[o] = nums[l - 1]
        return
    m = (l + r) // 2
    build(o * 2, l, m)
    build(o * 2 + 1, m + 1, r)
    maintain(o)

def maintain(o):
    # sum
    T[o] = T[o * 2] + T[o * 2 + 1]
    # max
    T[o] = max(T[o * 2], T[o * 2 + 1])

def do(o, l, r, val):
    if val is not None:
        # set
        T[o] = val * (r - l + 1)
        todo[o] = val
        # add
        T[o] += val * (r - l + 1)
        todo[o] += val

def query_and_update(o, l, r, L, R, val):
    if L <= l and r <= R:
        ans = T[o]
        do(o, l, r, val)
        return ans
    m = (l + r) // 2
    if todo[o]:
        do(o * 2, l, m, todo[o])
        do(o * 2 + 1, m + 1, r, todo[o])
        todo[o] = 0
    ans = 0
    if m >= L:
        # sum
        ans += query_and_update(o * 2, l, m, L, R, val)
        # max
        ans = max(ans, query_and_update(o * 2, l, m, L, R, val))
    if m < R:
        # sum
        ans += query_and_update(o * 2 + 1, m + 1, r, L, R, val)
        # max
        ans = max(ans, query_and_update(o * 2 + 1, m + 1, r, L, R, val))
    maintain(o)
    return ans

build(1, 1, n)
query_and_update(1, 1, n, l + 1, r + 1, val)
```

## Common Patterns

### Coordinate Compression

LC: 315, 327, 493, 1649, 2736

When values are large but sparse, map them to dense indices.

```py
# discretization
values = sorted(set(A))
v2i = {x: i for i, x in enumerate(values)}

# use segment tree on indices
ST = SegmentTree(0, len(values) - 1)
for x in A:
    ST._add(ST.root, v2i[x], 1)
```

### Segment Tree as DP Table

LC: 2407, 300

Use segment tree to efficiently query max/min of DP values over a range.

Pattern: `dp[x] = max(query(x-k, x-1)) + 1`, then update ST at position x.

```py
ST = SegmentTree(n)
for x in A:
    mx = ST.rangeMax(max(x - k, 0), x - 1)
    ST._set(x, mx + 1)
```

### Count Inversions / Smaller Elements

LC: 315, 493, 1649

Count how many elements to the left/right are smaller/larger. Use segment tree on sorted values, query prefix sum before adding current element.

```py
# coordinate compression
v2i = {x: i for i, x in enumerate(sorted(set(A)))}

ST = SegmentTree(len(v2i))
ans = []
for x in reversed(A):  # process right to left
    ans.append(ST.rangeSum(0, v2i[x] - 1))  # count smaller elements to the right
    ST._add(v2i[x], 1)
ans.reverse()
```

### Max Overlap / Booking Intervals

LC: 732, 731, 729, 699

Track maximum overlap count across all intervals. Use range add max with global max query.

Pattern: For each interval [lo, hi), `rangeAddMax(lo, hi-1, 1)`, then return root.mx.

```py
ST = SegmentTree(0, 10**9)
for lo, hi in intervals:
    ST.rangeAddMax(ST.root, 1, lo, hi - 1)
return ST.root.mx
```

## Properties

Given a segment tree with N leaves:

1. At most log(N) layers
2. 2N-1 segments (nodes) in total
3. Given root index = 1, for each node o:
   - Left child index = o * 2
   - Right child index = o * 2 + 1
4. Given root index = 1, the i-th leaf index = N + i (for ZKW tree)

## Complexity

- Build: O(n)
- Point update: O(log n)
- Point query: O(log n)
- Range query: O(log n + k) where k = number of segments returned
- Range update (with lazy): O(log n)

## Reference

- [花花酱 Segment Tree 线段树 - 刷题找工作 SP14](https://www.youtube.com/watch?v=rYBtViWXYeI)
- [LeetCode Discussion: 4 Approaches for Range Sum Query Mutable](https://leetcode.com/problems/range-sum-query-mutable/discuss/1205304/Python3-4-approaches)
- [CP-Algorithms: Segment Tree](https://cp-algorithms.com/data_structures/segment_tree.html)
- [残酷小讲座：线段树 by OTTFF](https://www.youtube.com/watch?v=s7vZDDpeR7w)
