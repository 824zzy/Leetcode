---
tags:
  - leetcode
  - hashtable
  - moc
---

# Hash Table

## When to Use

| Problem Signal | Technique |
|---|---|
| Find pair with sum = k | Two sum pattern (hash table stores complement) |
| Find pair with (sum/product/diff) % k = 0 | Two sum variant (hash table stores modulo) |
| Count pairs/triplets/tuples with condition | N-sum pattern (reduce to smaller subproblems) |
| Group elements by property (anagram, pattern) | Grouping pattern (use tuple/string as key) |
| Count frequency / find duplicates | Counter (frequency counting) |
| Track most recent occurrence | Hash table stores index |
| Bidirectional mapping (isomorphic) | Two hash tables (forward + backward) |
| Clone graph/linked list with random pointers | Hash table maps old node to new node |
| Find longest consecutive sequence | Union-find via hash table (store endpoints) |
| Compute slope/ratio between points | Normalize with gcd, use tuple as key |
| LRU cache / insertion order matters | dict (Python 3.7+ preserves insertion order) |
| OrderedDict needed (move_to_end) | OrderedDict for explicit ordering operations |
| Default values for missing keys | defaultdict(int/list/set) |

## Two Sum Pattern

Classic pattern: find pair where `A[i] + A[j] = target`. Store complement in hash table as you iterate.

### Basic Two Sum

LC 1, 167

```py
def twoSum(self, A: List[int], target: int) -> List[int]:
    seen = {}
    for i, x in enumerate(A):
        if x in seen:
            return [seen[x], i]
        seen[target - x] = i
```

### Two Sum Variant: Divisibility

LC 1010, 1497

If `(x + y) % k = 0`, then `y % k = (-x % k) % k = (k - x % k) % k`.

```py
def numPairsDivisibleByK(self, A: List[int], k: int) -> int:
    cnt = Counter()
    ans = 0
    for x in A:
        x %= k
        ans += cnt[(k - x) % k]
        cnt[x] += 1
    return ans
```

### Two Sum with Frequency

Count all pairs, not just find one.

```py
cnt = Counter(A)
ans = 0
for x in cnt:
    complement = target - x
    if complement in cnt:
        if x == complement:
            # same element: choose 2 from cnt[x]
            ans += cnt[x] * (cnt[x] - 1) // 2
        elif x < complement:
            # avoid double counting
            ans += cnt[x] * cnt[complement]
return ans
```

## N-Sum Pattern

Reduce N-sum to (N-1)-sum by fixing one element, then use hash table for the innermost level.

### 4Sum II

LC 454

Split into two 2-sums. Compute all `A[i] + B[j]`, store frequency in hash table, then check `C[k] + D[l]`.

```py
def fourSumCount(self, A, B, C, D):
    cnt = Counter()
    for a in A:
        for b in B:
            cnt[a + b] += 1

    ans = 0
    for c in C:
        for d in D:
            ans += cnt[-(c + d)]
    return ans
```

### 3Sum with Multiplicity

LC 923

Count triplets where `A[i] + A[j] + A[k] = target` (i < j < k).

```py
def threeSumMulti(self, A, target):
    cnt = Counter(A)
    ans = 0
    for i, x in enumerate(sorted(cnt)):
        for j, y in enumerate(sorted(cnt)):
            if j < i:
                continue
            z = target - x - y
            if z < y or z not in cnt:
                continue
            if x == y == z:
                # all three same
                ans += cnt[x] * (cnt[x] - 1) * (cnt[x] - 2) // 6
            elif x == y:
                # two same
                ans += cnt[x] * (cnt[x] - 1) // 2 * cnt[z]
            elif y == z:
                # two same
                ans += cnt[x] * cnt[y] * (cnt[y] - 1) // 2
            elif x < y < z:
                # all different
                ans += cnt[x] * cnt[y] * cnt[z]
    return ans % (10**9 + 7)
```

## Grouping Pattern

Use hash table to group elements by some normalized key.

### Group Anagrams

LC 49

```py
def groupAnagrams(self, words):
    groups = defaultdict(list)
    for w in words:
        key = tuple(sorted(w))  # or: ''.join(sorted(w))
        groups[key].append(w)
    return list(groups.values())
```

### Isomorphic Strings / Word Pattern

LC 205, 290

Use two hash tables to ensure bijection (one-to-one mapping).

```py
def isIsomorphic(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    s2t, t2s = {}, {}
    for i, j in zip(s, t):
        if i in s2t and s2t[i] != j:
            return False
        if j in t2s and t2s[j] != i:
            return False
        s2t[i] = j
        t2s[j] = i
    return True
```

### Flip Columns for Maximum Equal Rows

LC 1072

Rows that are equal or complementary can all become equal after column flips. Normalize each row to canonical form.

```py
def maxEqualRowsAfterFlips(self, matrix):
    cnt = Counter()
    for row in matrix:
        # normalize: flip row if it starts with 1
        key = tuple(row if row[0] == 0 else [1 - x for x in row])
        cnt[key] += 1
    return max(cnt.values())
```

### Max Points on a Line

LC 149

For each point, compute slope to all other points. Normalize slope as `(dy/gcd, dx/gcd)`.

```py
def maxPoints(self, points):
    ans = 0
    for i, (x1, y1) in enumerate(points):
        slopes = defaultdict(int)
        for j, (x2, y2) in enumerate(points):
            if i == j:
                continue
            if x1 == x2:
                slopes[(inf, inf)] += 1
            else:
                dx, dy = x1 - x2, y1 - y2
                g = gcd(dx, dy)
                slopes[(dy // g, dx // g)] += 1
        ans = max(ans, 1 + max(slopes.values(), default=0))
    return ans
```

## Frequency Counting

Use Counter for frequency-based queries.

### Counter Operations

1. `Counter.most_common(num)`: return a list contains tuple.
2. `del Counter[key]`: delete an item. or `Counter[key]=0`.
3. `cntA+cntB`: add two counters together.
4. `cntA-cntB`: subtract (keeping only positive counts).
5. `cntA&cntB`: find intersection of two counters. min(cntA, cntB)
6. `cntA|cntB`: find union of two counters. max(cntA, cntB)

### Find Common Characters

LC 1002

Find characters that appear in all strings with their minimum frequency.

```py
def commonChars(self, words):
    ans = Counter(words[0])
    for w in words:
        ans &= Counter(w)  # intersection
    return list(ans.elements())
```

### Top K Frequent Words

LC 692

```py
def topKFrequent(self, words, k):
    return [w for w, _ in sorted(Counter(words).most_common(),
                                  key=lambda t: (-t[1], t[0]))][:k]
```

### Array of Doubled Pairs

LC 954

Check if array can be paired such that one element is double of another.

```py
def canReorderDoubled(self, arr):
    cnt = Counter(arr)
    for x in sorted(cnt, key=abs):
        if cnt[x] > cnt[2 * x]:
            return False
        cnt[2 * x] -= cnt[x]
    return True
```

## Track Most Recent Occurrence

Store index in hash table to find minimum/maximum distance between duplicates.

### Minimum Consecutive Cards to Pick Up

LC 2260, 219

```py
def minimumCardPickup(self, cards):
    ans = inf
    last = {}
    for i, c in enumerate(cards):
        if c in last:
            ans = min(ans, i - last[c] + 1)
        last[c] = i
    return ans if ans < inf else -1
```

## Advanced Patterns

### Longest Consecutive Sequence

LC 128

Use hash table to store sequence endpoints. When inserting `x`, check if `x-1` and `x+1` exist, then merge sequences.

```py
def longestConsecutive(self, nums):
    mp = {}
    for x in nums:
        if x not in mp:
            l = mp.get(x - 1, 0)
            r = mp.get(x + 1, 0)
            length = l + r + 1
            mp[x] = mp[x - l] = mp[x + r] = length
    return max(mp.values(), default=0)
```

### Clone Graph / Linked List with Random Pointer

LC 133, 138

Use hash table to map original nodes to copied nodes.

```py
def copyRandomList(self, head):
    if not head:
        return None

    # first pass: create all nodes
    seen = {}
    curr = head
    while curr:
        seen[curr] = Node(curr.val)
        curr = curr.next

    # second pass: link next and random pointers
    curr = head
    while curr:
        if curr.next:
            seen[curr].next = seen[curr.next]
        if curr.random:
            seen[curr].random = seen[curr.random]
        curr = curr.next

    return seen[head]
```

### LRU Cache

LC 146

Python 3.7+ dict preserves insertion order. Use `pop` + re-insert to move to end.

```py
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache.pop(key)
            self.cache[key] = val  # move to end
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) == self.cap:
            # evict least recently used (first item)
            self.cache.pop(next(iter(self.cache)))
        self.cache[key] = value
```

## defaultdict Patterns

Use defaultdict when you need automatic initialization of missing keys.

### Group by Property

```py
groups = defaultdict(list)
for item in items:
    key = compute_key(item)
    groups[key].append(item)
```

### Count Nested Frequencies

```py
freq = defaultdict(lambda: defaultdict(int))
for item in items:
    category = get_category(item)
    freq[category][item] += 1
```

### Build Adjacency List

```py
graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)
```

## OrderedDict Patterns

Use OrderedDict when you need explicit control over insertion order (move_to_end, popitem).

### LRU Cache (Alternative Implementation)

```py
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)
```

## Key Insights

1. **Hash table = O(1) lookup**: The core advantage. Use it whenever you need to check existence or retrieve value in constant time.

2. **Complement pattern**: Instead of storing `x`, store `target - x`. This transforms "find two elements" into "check if one element exists".

3. **Normalize keys**: For grouping, normalize the key to canonical form (sorted tuple, gcd-reduced ratio, etc.) so equivalent items map to same key.

4. **Two hash tables for bijection**: When you need one-to-one mapping (isomorphic, word pattern), use two hash tables to check both directions.

5. **Counter arithmetic**: Use Counter's built-in operations (`+`, `-`, `&`, `|`) for set-like operations on multisets.

6. **Index as value**: Store indices (not just existence) to compute distances, ranges, or track first/last occurrence.

7. **Reduce N-sum to 2-sum**: Split N-sum problems into nested loops with hash table at the innermost level. For 4-sum, compute all 2-sums first, store in hash table, then check remaining 2-sums.

8. **Frequency map + sorted iteration**: When pairing elements with constraints (like doubling), iterate in sorted order by key and greedily consume from frequency map.

9. **Python dict is ordered (3.7+)**: You can use plain dict for LRU cache. Use OrderedDict only if you need `move_to_end` or `popitem(last=False)`.

10. **defaultdict saves boilerplate**: Use `defaultdict(int)` for counting, `defaultdict(list)` for grouping, `defaultdict(set)` for deduplication.
