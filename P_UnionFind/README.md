# Union-Find (Disjoint Set Union)

## When to Use

| Problem Signal | Technique |
|---|---|
| Track connected components in graph | Standard union-find |
| Detect cycle in undirected graph | Union returns false when already connected |
| Merge groups by equality/connectivity | Union on each constraint |
| Minimum spanning tree (MST) | Kruskal's algorithm |
| Count component sizes | Counter on find(x) for all elements |
| Dynamic connectivity queries | Union during updates, find for queries |
| Grid connectivity (2D islands) | Flatten to 1D: `row * n + col` |
| Group by transitive property (accounts, emails) | Union all related items, group by root |
| Find number of swaps to fix permutation | Union cycles, count edges minus roots |

## Standard Union-Find

Union-find maintains disjoint sets with two key optimizations:
1. **Path compression** during find: flattens tree by pointing directly to root
2. **Union by rank** (optional): merges smaller tree into larger tree

Time complexity: O(α(n)) per operation, where α is inverse Ackermann (effectively constant).

### Array-Based Implementation

Use when elements are integers in a known range [0, n).

```py
A = list(range(n))

def find(x):
    if A[x] != x:
        A[x] = find(A[x])  # path compression
    return A[x]

def union(x, y):
    A[find(x)] = find(y)

# alternative: return False if already connected
def union(x, y):
    xx, yy = find(x), find(y)
    if xx == yy:
        return False
    A[xx] = yy
    return True
```

### Dictionary-Based Implementation

Use when elements are non-contiguous, strings, tuples, or unknown range.

```py
dsu = {}

def find(x):
    if x not in dsu:
        dsu[x] = x
    elif dsu[x] != x:
        dsu[x] = find(dsu[x])
    return dsu[x]

def union(x, y):
    dsu[find(x)] = find(y)

# alternative: return False if already connected
def union(x, y):
    xx, yy = find(x), find(y)
    if xx == yy:
        return False
    dsu[xx] = yy
    return True
```

### Class-Based Implementation

Use when you need to track additional state (rank, size, count).

```py
class DSU:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)
```

### Weighted Union (Union by Size)

Track component sizes to optimize merging and answer size queries.

```py
class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xx, yy = find(x), find(y)
        if xx == yy:
            return
        # merge smaller into larger
        if self.size[xx] < self.size[yy]:
            xx, yy = yy, xx
        self.p[yy] = xx
        self.size[xx] += self.size[yy]

    def get_size(self, x):
        return self.size[self.find(x)]
```

## Kruskal's Algorithm (Minimum Spanning Tree)

Kruskal's algorithm builds an MST by greedily adding minimum-weight edges that don't create cycles. Union-find efficiently detects cycles.

Time complexity: O(E log E) for sorting edges, O(E α(V)) for union-find operations.

### Template

```py
class DSU:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)

# find all edges and sort by weight
edges = []
for i in range(len(A)):
    for j in range(i + 1, len(A)):
        dist = compute_distance(A[i], A[j])
        edges.append((dist, i, j))
edges.sort()

# greedily add edges if they connect different components
ans = 0
dsu = DSU(len(A))
for dist, i, j in edges:
    if dsu.find(i) != dsu.find(j):
        dsu.union(i, j)
        ans += dist
return ans
```

### Common MST problems

- LC 1584: Manhattan distance
- LC 1168: Water distribution with virtual source node
- LC 1489: Critical and pseudo-critical edges (MST variants)

## Common Patterns

### Pattern 1: Basic connectivity

LC 990, 323, 684, 1971

Two-pass approach: first union all equalities/edges, then check constraints.

```py
dsu = list(range(n))

# first pass: union all connections
for x, y in edges:
    union(x, y)

# second pass: verify constraints
for x, y in constraints:
    if find(x) == find(y):
        return False  # or count, etc.
return True
```

### Pattern 2: Count component sizes

LC 827, 2316, 952

After all unions, count elements per root.

```py
# after all unions
cnt = Counter(find(i) for i in range(n))
return max(cnt.values())
```

### Pattern 3: Grid connectivity

LC 827, 305, 1202

Flatten 2D grid to 1D indices: `index = row * n + col`.

```py
n = len(G)
A = list(range(n * n))

for x in range(n):
    for y in range(n):
        if G[x][y] == 1:
            for dx, dy in [(0, 1), (1, 0)]:  # only right and down
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and G[nx][ny] == 1:
                    union(x * n + y, nx * n + ny)
```

### Pattern 4: Group by transitive property

LC 721, 1202, 2157

Map items to indices, union related items, group by root.

```py
# map items to indices
item_to_idx = {item: i for i, item in enumerate(items)}

# union related items
for group in relations:
    for i in range(1, len(group)):
        union(item_to_idx[group[0]], item_to_idx[group[i]])

# collect groups
groups = defaultdict(list)
for item in items:
    groups[find(item_to_idx[item])].append(item)
```

### Pattern 5: Cycle detection in permutation

LC 765, 2493

Model permutation as graph where `A[i] -> i`. Each connected component is a cycle. Minimum swaps to fix = edges - components.

```py
dsu = DSU(n // 2)
swaps = 0
for i in range(0, n, 2):
    a, b = A[i] // 2, A[i + 1] // 2
    if dsu.find(a) != dsu.find(b):
        dsu.union(a, b)
        swaps += 1  # each union = one swap needed
return swaps
```

### Pattern 6: Union by prime factors

LC 952, 2709

For number connectivity problems, union numbers with their prime factors.

```py
dsu = DSU(max(A) + 1)
for x in A:
    # union x with all its prime factors
    for p in range(2, int(sqrt(x)) + 1):
        if x % p == 0:
            dsu.union(x, p)
            dsu.union(x, x // p)

cnt = Counter(dsu.find(x) for x in A)
return max(cnt.values())
```

## Key Insights

**When union-find beats DFS/BFS:**
- Many connectivity queries after batch updates
- Need to track component sizes efficiently
- MST problems (Kruskal's)

**Path compression is critical:** Without it, find degrades to O(n). Always use `if A[x] != x: A[x] = find(A[x])`.

**Two-pass pattern:** Often you need to union first (build components), then query second (check constraints).

**Grid flattening:** For 2D grids, `row * n + col` converts to 1D. Only check right and down neighbors to avoid duplicate unions.

**Counting components:** Use `len(set(find(i) for i in range(n)))` or track count during union.

**Dictionary DSU for sparse data:** When element space is large or non-numeric, dictionary-based DSU avoids wasting memory.

## Reference

- [Python 2 solutions: Kruskal & Prim](https://leetcode.com/problems/min-cost-to-connect-all-points/discuss/1476951/Python-2-solutions%3A-Kruskal-and-Prim-Standard-code-Clean-and-Concise)
- [Princeton Union-Find PDF](https://www.cs.princeton.edu/~rs/AlgsDS07/01UnionFind.pdf)
