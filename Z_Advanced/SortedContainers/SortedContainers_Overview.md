---
tags:
  - leetcode
  - advanced
  - moc
---

# Sorted Containers

Python's `sortedcontainers` library provides balanced tree data structures without the complexity of manual AVL/Red-Black tree implementations.

## When to Use

| Problem Signal | Tool | Why |
|---|---|---|
| Rank queries (kth smallest, count < x) | SortedList | O(log n) rank, O(log n) access by index |
| Dynamic median / percentile queries | SortedList | O(log n) insert, O(1) access by index |
| Maintain set with order statistics | SortedList | Combines set operations with indexing |
| Merge overlapping intervals dynamically | SortedList | O(log n) insert, easy neighbor access |
| Range queries with updates | Segment Tree / BIT | Better for point update + range query |
| Only need max/min, no middle ranks | Heap | O(1) peek, O(log n) insert |
| Need multiset (duplicates allowed) | SortedList | Default allows duplicates |

## SortedList API

Time complexity:

| Operation | Time | Method |
|---|---|---|
| Insert element | O(log n) | `sl.add(x)` |
| Remove element | O(log n) | `sl.remove(x)`, `sl.pop(idx)` |
| Access by index | O(log n) | `sl[idx]` |
| Binary search | O(log n) | `sl.bisect_left(x)`, `sl.bisect_right(x)` |
| Count occurrences | O(log n) | `sl.count(x)` |
| Check membership | O(log n) | `x in sl` |
| Size | O(1) | `len(sl)` |
| Clear | O(n) | `sl.clear()` |

### Bisect semantics

```py
sl = SortedList([1, 3, 3, 3, 5])

sl.bisect_left(3)   # 1 (leftmost position where 3 could be inserted)
sl.bisect_right(3)  # 4 (rightmost position where 3 could be inserted)
sl.bisect_left(4)   # 4 (same as bisect_right for non-existent element)

# count elements < x
cnt_less = sl.bisect_left(x)

# count elements <= x
cnt_leq = sl.bisect_right(x)

# count elements == x
cnt_eq = sl.bisect_right(x) - sl.bisect_left(x)

# count elements > x
cnt_greater = len(sl) - sl.bisect_right(x)
```

## Common Patterns

### Pattern 1: Dynamic rank queries

LC 1649, 2519

Track how many elements are less/greater than current element as you insert.

```py
sl = SortedList()
for x in nums:
    less = sl.bisect_left(x)
    greater = len(sl) - sl.bisect_right(x)
    # process rank statistics
    sl.add(x)
```

### Pattern 2: Dynamic median / percentile

LC 480 (sliding window median), 295 (find median from data stream)

```py
sl = SortedList()
for x in stream:
    sl.add(x)
    # median is at middle index
    median = sl[len(sl) // 2]
```

### Pattern 3: Maintain two sorted views

LC 716 (Max Stack)

Keep two SortedLists to support different orderings.

```py
stack = SortedList()  # sorted by insertion order (idx, val)
values = SortedList()  # sorted by value (val, idx)

# push
stack.add((cnt, x))
values.add((x, cnt))

# pop max
val, idx = values.pop()
stack.remove((idx, val))
```

### Pattern 4: Merge overlapping intervals dynamically

LC 352, 2276, 715

When adding interval `[left, right]`, merge all overlapping intervals using bisect to find neighbors.

```py
sl = SortedList()  # stores non-overlapping intervals

def add_interval(left, right):
    # find first interval that might overlap
    k = sl.bisect_left((left, right))

    # merge all overlapping intervals to the right
    while k < len(sl) and sl[k][0] <= right:
        l, r = sl.pop(k)
        right = max(right, r)

    # merge with left neighbor if overlapping
    if k and left <= sl[k-1][1]:
        l, r = sl.pop(k-1)
        left = l
        right = max(right, r)

    sl.add((left, right))
```

**Key insight**: Store intervals as tuples `(left, right)`. Python sorts tuples lexicographically, so intervals are ordered by left endpoint, then right endpoint.

**Merge condition**: Two intervals `[a, b]` and `[c, d]` overlap if `a <= d` and `c <= b`. Simplifies to `c <= b` when `c >= a` (already sorted).

### Pattern 5: 132 pattern detection

LC 456

Maintain a SortedList of candidates while scanning. Use bisect to check if current element fits the pattern.

```py
sl = SortedList()
for num in nums:
    # check if there exists element in sl that satisfies condition
    idx = sl.bisect_left(num)
    if idx < len(sl):
        # found candidate
        return True
    sl.add(num)
```

## Merge Intervals Variations

### Static merge (one-time)

LC 56, 57

Sort intervals by start time, then scan and merge adjacent overlapping intervals.

```py
intervals.sort()
merged = [intervals[0]]
for start, end in intervals[1:]:
    if start <= merged[-1][1]:
        merged[-1][1] = max(merged[-1][1], end)
    else:
        merged.append([start, end])
```

### Dynamic merge with queries

LC 352, 2276, 715, 732

Use SortedList to maintain non-overlapping intervals and merge on insertion (see Pattern 4).

### Range module pattern

LC 715

Track covered ranges. Support `addRange`, `removeRange`, `queryRange`.

```py
# add: merge all overlapping intervals
# remove: split intervals that overlap with removed range
# query: check if [left, right) is fully covered by one interval
```

### Sweep line for max overlap count

LC 218, 732

Alternative to SortedList: use event-based sweep line with sorted events.

```py
events = []
for start, end in intervals:
    events.append((start, 1))
    events.append((end, -1))
events.sort()

count = 0
max_overlap = 0
for pos, delta in events:
    count += delta
    max_overlap = max(max_overlap, count)
```

## Decision Guide: SortedList vs Other Tools

### When NOT to use SortedList

1. **Only need min/max**: Use a heap. O(1) peek vs O(log n) access.
2. **Range sum/min/max with point updates**: Use Segment Tree or BIT. O(log n) range query vs O(n) with SortedList.
3. **Static data with one-time sort**: Just use `sorted()`. O(n log n) vs O(n log n) but simpler.
4. **Interval scheduling (greedy)**: Sort once and scan. No need for dynamic structure.

### When SortedList shines

1. **Need both insertion and rank queries**: Can't do this with heap alone.
2. **Dynamic median/percentile**: Perfect fit. Heap-based solutions are painful.
3. **Merge intervals with queries in between**: Much cleaner than manual tree.
4. **Need to maintain order AND do lookups**: Set + order maintenance.

## LeetCode References

### Core SortedList usage
- LC 456: 132 Pattern
- LC 1649: Create Sorted Array through Instructions
- LC 2349: Design a Number Container System
- LC 2426: Number of Pairs Satisfying Inequality
- LC 2519: Count the Number of K-Big Indices

### Dynamic median / rank queries
- LC 295: Find Median from Data Stream (classic)
- LC 480: Sliding Window Median

### Merge intervals dynamically
- LC 56: Merge Intervals (static)
- LC 57: Insert Interval (static + one insert)
- LC 352: Data Stream as Disjoint Intervals
- LC 715: Range Module
- LC 2276: Count Integers in Intervals

### Design problems
- LC 716: Max Stack
- LC 2336: Smallest Number in Infinite Set
- LC 2353: Design a Food Rating System

### Advanced / multi-technique
- LC 218: The Skyline Problem (sweep line alternative)
- LC 699: Falling Squares
- LC 732: My Calendar III