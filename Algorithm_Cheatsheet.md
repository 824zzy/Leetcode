---
tags:
  - leetcode
  - cheatsheet
---

# Algorithm Templates Cheat Sheet

## Table of Contents

1. [Binary Search](#binary-search)
2. [Two Pointers](#two-pointers)
3. [Sliding Window](#sliding-window)
4. [Prefix Sum & Difference Array](#prefix-sum--difference-array)
5. [Hash Table](#hash-table)
6. [Linked List](#linked-list)
7. [Stack (Monotonic Stack & Tree Traversal)](#stack)
8. [Queue (Monotonic Queue)](#monotonic-queue)
9. [Tree DFS](#tree-dfs)
10. [BFS (Graph & Tree)](#bfs)
11. [Backtracking](#backtracking)
12. [Union Find](#union-find)
13. [Trie](#trie)
14. [Dynamic Programming](#dynamic-programming)
15. [Shortest Path (Dijkstra & Floyd-Warshall)](#shortest-path)
16. [Minimum Spanning Tree (Kruskal & Prim)](#minimum-spanning-tree)
17. [Segment Tree](#segment-tree)
18. [Binary Indexed Tree (Fenwick Tree)](#binary-indexed-tree)
19. [Pattern Searching (KMP)](#pattern-searching-kmp)
20. [Bit Manipulation](#bit-manipulation)
21. [Math](#math)
22. [Sorting (Cycle Sort)](#sorting)
23. [Majority Voting (Boyer-Moore)](#majority-voting)

---

## Binary Search

Signal: mini-max / max-mini, sorted array, monotonicity.

```py
def binary_search(self, A: List[int], t: int) -> int:
    l, r = 0, len(A)
    while l < r:
        m = (l + r) // 2
        if A[m] > t: r = m
        else: l = m + 1
    return l
```

**Bisect module**: `bisect_left(A, x)`, `bisect_right(A, x)`, `insort(A, x)`

---

## Two Pointers

**Same direction:**

```py
i = 0
for j in range(len(A)):
    if/while LOGIC:
        MOVE_i
    UPDATE_answer
```

**Opposite direction:**

```py
l, r = 0, len(A) - 1
while l <= r:
    # logic for A and ans
```

---

## Sliding Window

**Fixed window:**

```py
sm = # init first k elements
ans = # init answer
for i in range(k, len(A)):
    # update sm
    # update ans
```

**Dynamic window:**

```py
i = 0
for j in range(len(A)):
    # update cnt/container
    while/if LOGIC:
        # update i
    # update answer
```

**At-most-K difference (count subarrays with exactly K distinct):**

```py
def atMost(A, k):
    cnt = Counter()
    i, ans = 0, 0
    for j in range(len(A)):
        cnt[A[j]] += 1
        while len(cnt) > k:
            cnt[A[i]] -= 1
            if cnt[A[i]] == 0: del cnt[A[i]]
            i += 1
        ans += j - i + 1
    return ans
return atMost(A, k) - atMost(A, k - 1)
```

---

## Prefix Sum & Difference Array

**1D prefix sum:** `itertools.accumulate(A)`

**2D prefix sum:**

```py
m, n = len(A), len(A[0])
prefix = [[0] * (n + 1) for _ in range(m + 1)]
for i in range(m):
    for j in range(n):
        prefix[i+1][j+1] = A[i][j] + prefix[i][j+1] + prefix[i+1][j] - prefix[i][j]
```

**Difference array (sweep line):**

```py
diff = [0] * (n + 1)
for i, j in intervals:
    diff[i] += 1
    diff[j + 1] -= 1
# accumulate to get counts
```

**Prefix sum + hash table (count subarrays with sum = k):**

```py
cnt = Counter([0])
ans = prefix = 0
for x in A:
    prefix += x
    ans += cnt[prefix - k]
    cnt[prefix] += 1
```

**Prefix sum + hash table (longest subarray with sum = k):**

```py
cnt = {0: -1}
prefix = ans = 0
for i, x in enumerate(A):
    prefix += x
    if prefix - k in cnt: ans = max(ans, i - cnt[prefix - k])
    cnt.setdefault(prefix, i)
```

---

## Hash Table

**Counter operations:** `most_common(n)`, `cntA + cntB`, `cntA - cntB` (positive only), `cntA & cntB` (min), `cntA | cntB` (max)

---

## Linked List

**Dummy head template:**

```py
pre = ans = ListNode('inf')
pre.next = head
cur = head
while CONDITION:
    # logic to delete, insert, etc.
return ans.next
```

**Reverse linked list:**

```py
pre = None
while head:
    pre, head.next, head = head, pre, head.next
return pre
```

---

## Stack

### Monotonic Stack

Use **increasing stack** to find **next smaller**, **decreasing stack** to find **next greater**.

**Next smaller on both sides:**

```py
# next smaller on the right
R = [len(A)] * len(A)
stk = []
for i in range(len(A)):
    while stk and A[stk[-1]] > A[i]:
        R[stk.pop()] = i
    stk.append(i)

# next smaller on the left
L = [-1] * len(A)
stk = []
for i in reversed(range(len(A))):
    while stk and A[stk[-1]] >= A[i]:
        L[stk.pop()] = i
    stk.append(i)
```

**Next greater on both sides:**

```py
R = [len(A)] * len(A)
stk = []
for i in range(len(A)):
    while stk and A[stk[-1]] < A[i]:
        R[stk.pop()] = i
    stk.append(i)
```

### Eulerian Path (Hierholzer's Algorithm)

```py
def hierholzer(pairs):
    G = defaultdict(list)
    degree = defaultdict(int)
    for i, j in pairs:
        G[i].append(j)
        degree[i] += 1
        degree[j] -= 1
    x = next(n for n in degree if degree[n] == 1)
    ans, stk = [], [x]
    while stk:
        while G[stk[-1]]:
            stk.append(G[stk[-1]].pop())
        ans.append(stk.pop())
    ans.reverse()
    return [[ans[i], ans[i+1]] for i in range(len(ans) - 1)]
```

### Iterative Tree Traversal

```py
def preOrder(root):
    ans, stk, node = [], [], root
    while stk or node:
        if node:
            ans.append(node.val)
            stk.append(node)
            node = node.left
        else:
            node = stk.pop().right
    return ans

def inOrder(root):
    ans, stk, node = [], [], root
    while stk or node:
        if node:
            stk.append(node)
            node = node.left
        else:
            node = stk.pop()
            ans.append(node.val)
            node = node.right
    return ans

def postOrder(root):
    stk1, stk2, ans = [root], [], []
    while stk1:
        node = stk1.pop()
        if node.left: stk1.append(node.left)
        if node.right: stk1.append(node.right)
        stk2.append(node)
    while stk2: ans.append(stk2.pop().val)
    return ans
```

---

## Monotonic Queue

```py
q = deque()  # monotonic decreasing queue
ans = []
for i, x in enumerate(A):
    while q and A[q[-1]] <= x: q.pop()       # maintain monotonicity
    q.append(i)
    while q and i - q[0] >= k: q.popleft()   # evict out-of-window
    if i >= k - 1:
        ans.append(A[q[0]])
```

---

## Tree DFS

**Recursive:**

```py
def dfs(node, args):
    if not node: return 0
    l = dfs(node.left)
    r = dfs(node.right)
    # do sth
    return # sth
```

**Level order:**

```py
Q = [root]
while Q:
    nxtQ = []
    for node in Q:
        if node.left: nxtQ.append(node.left)
        if node.right: nxtQ.append(node.right)
    Q = nxtQ
```

**Lowest Common Ancestor:**

```py
def lca(node, p, q):
    if not node or node == p or node == q: return node
    l = lca(node.left, p, q)
    r = lca(node.right, p, q)
    if l and r: return node
    return l or r
```

**Binary Lifting (k-th ancestor in O(log n)):**

```py
class TreeAncestor:
    def __init__(self, n, parent):
        m = 1 + int(log2(n))
        self.dp = [[-1] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if j == 0: self.dp[i][0] = parent[i]
                elif self.dp[i][j-1] != -1:
                    self.dp[i][j] = self.dp[self.dp[i][j-1]][j-1]

    def getKthAncestor(self, node, k):
        while k > 0 and node != -1:
            i = int(log2(k))
            node = self.dp[node][i]
            k -= (1 << i)
        return node
```

---

## BFS

**Graph BFS:**

```py
Q = [START_STATE]
seen = set()
while Q:
    i = Q.pop(0)
    if i not in seen:
        seen.add(i)
        for NEXT in NEIGHBORS:
            if CONDITION:
                Q.append(NEXT)
```

**Matrix DFS/BFS:**

```py
M, N = len(A), len(A[0])
D = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def dfs(x, y):
    for dx, dy in D:
        if 0 <= x+dx < M and 0 <= y+dy < N and CONDITION:
            dfs(x+dx, y+dy)
```

**Histogram model (for maximal rectangle problems):**

```py
hist = [0] * len(A[0])
for i in range(len(A)):
    for j in range(len(A[0])):
        hist[j] = hist[j] + 1 if A[i][j] else 0
```

---

## Backtracking

**Array type:**

```py
ans, stk = [], []
def dfs(i):
    if CONDITION: return ans.append(stk.copy())
    for j in range(ARG):
        stk.append(A[j])
        dfs(j)
        stk.pop()
dfs(0)
```

**Grid type:**

```py
D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def dfs(x, y):
    if CONDITION: return
    tmp = A[x][y]
    A[x][y] = '#'
    for dx, dy in D:
        if 0 <= x+dx < len(A) and 0 <= y+dy < len(A[0]) and CONDITION:
            dfs(x+dx, y+dy)
    A[x][y] = tmp
```

---

## Union Find

**Array-based:**

```py
A = list(range(n + 1))
def find(x):
    if A[x] != x: A[x] = find(A[x])
    return A[x]
def union(x, y):
    xx, yy = find(x), find(y)
    if xx == yy: return False
    A[xx] = yy
    return True
```

**Dictionary-based:**

```py
dsu = {}
def find(x):
    if x not in dsu: dsu[x] = x
    elif dsu[x] != x: dsu[x] = find(dsu[x])
    return dsu[x]
def union(x, y):
    dsu[find(x)] = find(y)
```

---

## Trie

**Full class:**

```py
class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word):
        node = self.trie
        for c in word:
            if c not in node: node[c] = {}
            node = node[c]
        node['#'] = word

    def search(self, word):
        node = self.trie
        for c in word:
            if c not in node: return False
            node = node[c]
        return '#' in node

    def startsWith(self, prefix):
        node = self.trie
        for c in prefix:
            if c not in node: return False
            node = node[c]
        return True
```

**Contest shorthand:**

```py
trie = {}
for word in words:
    node = trie
    for c in word:
        node = node.setdefault(c, {})
    node['#'] = word
```

---

## Dynamic Programming

### Kadane's Algorithm (Maximum Subarray)

```py
ans, cur = -inf, 0
for x in A:
    cur = max(x, cur + x)
    ans = max(ans, cur)
```

### Longest Increasing Subsequence

```py
# O(N^2)
dp = [1] * len(A)
for i in range(len(A)):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# O(NlogN) with bisect
def LIS(A):
    dp = []
    for x in A:
        k = bisect_left(dp, x)
        if k == len(dp): dp.append(x)
        else: dp[k] = x
    return len(dp)
```

### Knapsack

**0/1 Knapsack:**

```py
@cache
def dp(i):
    if CONDITION: return ?
    skip = ...
    take = ...
    return ?(skip, take)
```

**Unbounded Knapsack:**

```py
@cache
def dp(n):
    if n == 0: return 0
    if n < 0: return inf
    return min(1 + dp(n - c) for c in coins)
```

### Digit DP (Most Popular Template)

```py
high = str(n)
n = len(high)
low = str(0).zfill(n)

@cache
def dfs(i, limit_low, limit_high, is_num):
    if i == n: return 1
    ans = 0
    if not is_num and low[i] == '0':
        ans += dfs(i+1, True, False, False)
    lo = int(low[i]) if limit_low else 0
    hi = int(high[i]) if limit_high else 9
    d0 = 0 if is_num else 1
    for d in range(max(lo, d0), hi + 1):
        ans += dfs(i+1, limit_low and d == lo, limit_high and d == hi, True)
    return ans
```

### Matrix Exponentiation

```py
MOD = 10**9 + 7

def mul(a, b):
    return [[sum(x * y for x, y in zip(row, col)) % MOD for col in zip(*b)] for row in a]

def pow_mul(a, n, f0):
    res = f0
    while n:
        if n & 1: res = mul(a, res)
        a = mul(a, a)
        n >>= 1
    return res
```

---

## Shortest Path

### Dijkstra (Single Source, O(E log V))

```py
G = [[] for _ in range(n + 1)]
for i, j, w in edges:
    G[i].append((j, w))

pq = [(0, src)]
dis = [inf] * (n + 1)
while pq:
    d, i = heappop(pq)
    if d > dis[i]: continue
    for j, w in G[i]:
        if d + w < dis[j]:
            dis[j] = d + w
            heappush(pq, (d + w, j))
```

### Floyd-Warshall (All Pairs, O(V^3))

```py
dist = [[inf] * n for _ in range(n)]
for i, j, w in edges: dist[i][j] = dist[j][i] = w
for i in range(n): dist[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```

---

## Minimum Spanning Tree

### Kruskal's (Union Find + Sorted Edges)

```py
class DSU:
    def __init__(self, n):
        self.p = list(range(n))
    def find(self, x):
        if self.p[x] != x: self.p[x] = self.find(self.p[x])
        return self.p[x]
    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)

edges.sort()  # sort by weight
dsu = DSU(n)
ans = 0
for dist, i, j in edges:
    if dsu.find(i) != dsu.find(j):
        dsu.union(i, j)
        ans += dist
```

### Prim's (Heap-based)

```py
seen = set()
pq = [(0, 0)]  # (dist, vertex)
total = 0
while len(seen) < n:
    dist, u = heappop(pq)
    if u in seen: continue
    seen.add(u)
    total += dist
    for v, d in G[u].items():
        if v not in seen:
            heappush(pq, (d, v))
```

---

## Segment Tree

### ZKW Segment Tree (Compact)

```py
class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.T = [0] * 2 * n

    def _build(self, A):
        for i in range(self.n):
            self.T[i + self.n] = A[i]
        for i in reversed(range(self.n)):
            self.T[i] = self.T[2*i] + self.T[2*i+1]

    def _add(self, i, val):
        i += self.n
        diff = val - self.T[i]
        while i:
            self.T[i] += diff
            i //= 2

    def rangeSum(self, l, r):
        ans = 0
        l, r = l + self.n, r + self.n
        while l <= r:
            if l % 2: ans, l = ans + self.T[l], l + 1
            if not r % 2: ans, r = ans + self.T[r], r - 1
            l, r = l // 2, r // 2
        return ans
```

### Tree-based Segment Tree (with Lazy Propagation)

```py
class Node:
    def __init__(self, lo, hi, sm=0, mx=0, lazy=None):
        self.lo, self.hi = lo, hi
        self.sm, self.mx, self.lazy = sm, mx, lazy
        self.left = self.right = None

class SegmentTree:
    def __init__(self, lo, hi, A=[]):
        self.root = self._build(lo, hi, A) if A else Node(lo, hi)

    def _build(self, lo, hi, A):
        node = Node(lo, hi)
        if lo == hi:
            node.sm = node.mx = A[lo]
        else:
            m = (lo + hi) // 2
            node.left = self._build(lo, m, A)
            node.right = self._build(m+1, hi, A)
            node.sm = node.left.sm + node.right.sm
            node.mx = max(node.left.mx, node.right.mx)
        return node

    def _add(self, node, i, val):
        if node.lo == node.hi:
            node.sm += val; node.mx += val; return
        m = (node.lo + node.hi) // 2
        if not node.left:
            node.left = Node(node.lo, m)
            node.right = Node(m+1, node.hi)
        if i <= m: self._add(node.left, i, val)
        else: self._add(node.right, i, val)
        node.sm = node.left.sm + node.right.sm
        node.mx = max(node.left.mx, node.right.mx)

    def _sumQuery(self, node, lo, hi):
        if not node: return 0
        if node.lo == lo and node.hi == hi: return node.sm
        m = (node.lo + node.hi) // 2
        if hi <= m: return self._sumQuery(node.left, lo, hi)
        if lo > m: return self._sumQuery(node.right, lo, hi)
        return self._sumQuery(node.left, lo, m) + self._sumQuery(node.right, m+1, hi)
```

---

## Binary Indexed Tree

```py
class BIT:
    def __init__(self, n):
        self.A = [0] * (n + 1)

    def sum(self, k):
        sm, k = 0, k + 1
        while k:
            sm += self.A[k]
            k -= k & -k
        return sm

    def add(self, k, x):
        k += 1
        while k < len(self.A):
            self.A[k] += x
            k += k & -k
```

Caveat: `bit.sum(x-1)` = count of elements < x, `i - bit.sum(x)` = count of elements > x

---

## Pattern Searching (KMP)

```py
def getLPS(s):
    i, lps = 0, [0] * len(s)
    for j in range(1, len(s)):
        while s[j] != s[i] and i: i = lps[i-1]
        if s[j] == s[i]: i += 1
        lps[j] = i
    return lps

lps = getLPS(p)
i = 0
for j in range(len(s)):
    while s[j] != p[i] and i: i = lps[i-1]
    if s[j] == p[i]: i += 1
    if i == len(p): return j - len(p) + 1
return -1
```

---

## Bit Manipulation

**Common operations:**

| Operation | Code |
|---|---|
| Get i-th bit | `(x >> i) & 1` |
| Set i-th bit | `x \| (1 << i)` |
| Flip i-th bit | `x ^ (1 << i)` |
| Lowest set bit | `x & -x` |
| Clear lowest set bit | `x & (x - 1)` |
| Flip all n bits | `x ^= (1 << n) - 1` |
| String to bitmask | `mask \|= 1 << (ord(c) - ord('a'))` |

**Bitmask DP:**

```py
@cache
def dp(mask):
    for j in range(n):
        if mask & (1 << j):
            dp(mask ^ (1 << j))
```

---

## Math

**Arithmetic:** `n * (a1 + an) / 2`

**GCD/LCM:** `math.gcd(x, y)`, `math.comb(n, k)`

**Sieve of Eratosthenes:**

```py
def findPrimes(n):
    sieve = [1] * n
    sieve[0] = sieve[1] = 0
    for i in range(int(sqrt(n)) + 1):
        if sieve[i]:
            for j in range(i*i, n, i):
                sieve[j] = 0
    return [i for i in range(n) if sieve[i]]
```

**Prime factorization:**

```py
ans, d = set(), 2
while d * d <= x:
    if x % d == 0:
        ans.add(d)
        while x % d == 0: x //= d
    d += 1
if x > 1: ans.add(x)
```

**Least Prime Factor (sieve):**

```py
LPF = [0] * n
for i in range(2, n):
    if LPF[i] == 0:
        for j in range(i, n, i):
            if LPF[j] == 0: LPF[j] = i
```

---

## Sorting

### Cycle Sort (minimum swaps to sort)

```py
def cyclesort(A):
    mp = {x: i for i, x in enumerate(sorted(A))}
    seen = {x: False for x in A}
    ans = 0
    for i, x in enumerate(A):
        cnt = 0
        while i != mp[x] and not seen[x]:
            cnt += 1
            seen[x] = True
            i = mp[x]
            x = A[i]
        ans += max(0, cnt - 1)
    return ans
```

---

## Majority Voting

### Boyer-Moore Voting Algorithm

Find element appearing > N/2 times:

```py
cnt, cand = 0, None
for x in A:
    if x == cand: cnt += 1
    elif cnt == 0: cand = x
    else: cnt -= 1
return cand
```
