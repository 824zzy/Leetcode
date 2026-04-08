---
tags:
  - leetcode
  - searching
  - moc
---

# Dijkstra Algorithm for Single-Source Shortest Paths

## When to Use

| Problem Signal | Technique |
|---|---|
| Shortest path in weighted graph (positive weights) | Standard Dijkstra |
| 0-1 edge weights (free/costly moves) | 0-1 BFS (deque) |
| Minimize maximum edge (not sum of edges) | Modified Dijkstra (track max not sum) |
| Shortest path with constraints (k stops, discounts) | Dijkstra with extended state |
| Shortest path with state tracking (visited nodes, steps) | Dijkstra with bitmask/tuple state |
| Bidirectional shortest path (two sources, one dest) | Run Dijkstra from multiple sources + combine |
| Graph with modifiable edges | Dijkstra + binary search or iterative edge adjustment |

## Standard Dijkstra

### Key Insight

Breadth-first search is just Dijkstra's algorithm with all edge weights equal to 1. Dijkstra is conceptually BFS that respects edge costs by using a min-heap to always explore the cheapest next step.

### Template: Single-Source Shortest Path

Time: O(E log V) where E = edges, V = vertices

LC 743, 1334, 2642

```py
# Build adjacency list
G = [[] for _ in range(n)]
for i, j, w in edges:
    G[i].append((j, w))

# Initialize
pq = [(0, src)]
dis = [inf] * n
dis[src] = 0

# Dijkstra
while pq:
    d, i = heappop(pq)
    if d > dis[i]:
        continue
    for j, w in G[i]:
        new_d = d + w
        if new_d < dis[j]:
            dis[j] = new_d
            heappush(pq, (new_d, j))
```

### Template: Grid-Based (4-directional movement)

LC 1631, 2577

```py
pq = [(0, 0, 0)]  # (cost, x, y)
D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
dis = [[inf] * n for _ in range(m)]
dis[0][0] = 0

while pq:
    d, x, y = heappop(pq)
    if d > dis[x][y]:
        continue
    if x == m - 1 and y == n - 1:
        return d
    for dx, dy in D:
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n:
            new_d = d + cost(x, y, nx, ny)
            if new_d < dis[nx][ny]:
                dis[nx][ny] = new_d
                heappush(pq, (new_d, nx, ny))
```

### Variant: Using Seen Set Instead of Distance Array

Useful when you want to terminate early at destination and don't need all distances.

LC 1368, 2290

```py
pq = [(0, src)]
seen = set()

while pq:
    cost, i = heappop(pq)
    if i == dest:
        return cost
    if i in seen:
        continue
    seen.add(i)
    for j, w in G[i]:
        if j not in seen:
            heappush(pq, (cost + w, j))
```

### Variant: Bidirectional (Multiple Sources)

Run Dijkstra from multiple sources and combine results at each potential meeting point.

LC 2203

```py
def dijkstra(G, src):
    pq = [(0, src)]
    dis = [inf] * n
    dis[src] = 0
    while pq:
        d, i = heappop(pq)
        if d > dis[i]:
            continue
        for j, w in G[i]:
            if d + w < dis[j]:
                dis[j] = d + w
                heappush(pq, (d + w, j))
    return dis

# Run from src1, src2, and dest (on reversed graph)
dis1 = dijkstra(G, src1)
dis2 = dijkstra(G, src2)
dis3 = dijkstra(reverse_G, dest)

# Find best meeting point
ans = min(dis1[i] + dis2[i] + dis3[i] for i in range(n))
```

## 0-1 BFS

### Key Insight

When edges have only 0 or 1 weight, use a deque instead of a heap. Add 0-cost edges to the front, 1-cost edges to the back. This is O(V + E) instead of O(E log V).

### Template

LC 1368, 2290

```py
Q = deque([(0, 0)])  # (cost, node)
dis = [inf] * n
dis[0] = 0

while Q:
    d, i = Q.popleft()
    if d > dis[i]:
        continue
    for j, w in G[i]:
        new_d = d + w
        if new_d < dis[j]:
            dis[j] = new_d
            if w == 0:
                Q.appendleft((new_d, j))
            else:
                Q.append((new_d, j))
```

Grid variant (free moves in certain directions, costly otherwise):

```py
D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
Q = deque([(0, 0, 0)])
seen = set()

while Q:
    cost, x, y = Q.popleft()
    if (x, y) == (m - 1, n - 1):
        return cost
    if (x, y) in seen:
        continue
    seen.add((x, y))
    for dx, dy in D:
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in seen:
            if is_free_direction(x, y, dx, dy):
                Q.appendleft((cost, nx, ny))
            else:
                Q.append((cost + 1, nx, ny))
```

## Modified Distance Metric

### Key Insight

Sometimes you want to minimize the maximum edge on the path (bottleneck), not the sum of edges. The only change is how you compute the new distance.

### Template: Minimize Maximum Edge

LC 1631, 778

```py
pq = [(0, src)]
dis = [inf] * n
dis[src] = 0

while pq:
    max_edge, i = heappop(pq)
    if max_edge > dis[i]:
        continue
    for j, w in G[i]:
        new_max = max(max_edge, w)  # NOT max_edge + w
        if new_max < dis[j]:
            dis[j] = new_max
            heappush(pq, (new_max, j))
```

### Template: Maximize Product of Probabilities

LC 1514

```py
pq = [(-1.0, src)]  # negative because heapq is min-heap
prob = [0.0] * n
prob[src] = 1.0

while pq:
    p, i = heappop(pq)
    p = -p
    if p < prob[i]:
        continue
    for j, edge_prob in G[i]:
        new_p = p * edge_prob
        if new_p > prob[j]:
            prob[j] = new_p
            heappush(pq, (-new_p, j))
```

## Dijkstra with Extended State

### Key Insight

When the problem has constraints (max k stops, discounts available, time limits), extend the state to (cost, node, constraint_value). The seen set or distance array must also track this extended state.

### Template: With Step/Stop Limit

LC 787, 1928

```py
pq = [(0, src, 0)]  # (cost, node, steps)
seen = {}  # {(node, steps): cost}

while pq:
    cost, i, steps = heappop(pq)
    if i == dest:
        return cost
    if steps > k:
        continue
    for j, w in G[i]:
        new_cost = cost + w
        # Allow revisiting if we have fewer steps or lower cost
        if (j, steps + 1) not in seen or new_cost < seen[(j, steps + 1)]:
            seen[(j, steps + 1)] = new_cost
            heappush(pq, (new_cost, j, steps + 1))
```

### Template: With Discount/Special Moves

LC 2093

```py
pq = [(0, src, discounts)]  # (cost, node, discounts_left)
seen = {}  # {(node, discounts_left): cost}
seen[(src, discounts)] = 0

while pq:
    cost, i, d = heappop(pq)
    if i == dest:
        return cost
    for j, w in G[i]:
        # Option 1: normal move
        if (j, d) not in seen or cost + w < seen[(j, d)]:
            seen[(j, d)] = cost + w
            heappush(pq, (cost + w, j, d))
        # Option 2: use discount
        if d > 0:
            discounted = cost + w // 2
            if (j, d - 1) not in seen or discounted < seen[(j, d - 1)]:
                seen[(j, d - 1)] = discounted
                heappush(pq, (discounted, j, d - 1))
```

### Template: With Bitmask (Visit All Nodes)

LC 847

```py
pq = [(0, i, 1 << i) for i in range(n)]  # start from all nodes
heapify(pq)
seen = set((i, 1 << i) for i in range(n))
target = (1 << n) - 1

while pq:
    steps, i, mask = heappop(pq)
    if mask == target:
        return steps
    for j in G[i]:
        new_mask = mask | (1 << j)
        if (j, new_mask) not in seen:
            seen.add((j, new_mask))
            heappush(pq, (steps + 1, j, new_mask))
```

## When to Use Dijkstra vs Other Shortest Path Algorithms

### Dijkstra vs BFS
- Use **BFS** when all edges have weight 1 (or no weights)
- Use **Dijkstra** when edges have different positive weights
- Time: BFS is O(V + E), Dijkstra is O(E log V)

### Dijkstra vs 0-1 BFS
- Use **0-1 BFS** when edges have only 0 or 1 weight
- Use **Dijkstra** when edges have arbitrary positive weights
- Time: 0-1 BFS is O(V + E), Dijkstra is O(E log V)

### Dijkstra vs Floyd-Warshall
- Use **Dijkstra** for single-source or few sources (run multiple times)
- Use **Floyd-Warshall** for all-pairs shortest path on small graphs (n ≤ 400)
- Time: Dijkstra is O(E log V) per source, Floyd-Warshall is O(V³) for all pairs

### Dijkstra vs Bellman-Ford
- Use **Dijkstra** when all edge weights are non-negative
- Use **Bellman-Ford** when negative edges exist (Dijkstra fails with negative edges)
- Time: Dijkstra is O(E log V), Bellman-Ford is O(VE)

## Common Patterns

### Early Termination
If you only need distance to one destination, return immediately when popping the destination from the heap (don't wait for the heap to empty).

```py
while pq:
    d, i = heappop(pq)
    if i == dest:
        return d
    # ... rest of Dijkstra
```

### Deduplication (Skip Stale Entries)
The `if d > dis[i]: continue` check is critical. Without it, you may process the same node multiple times with worse distances, leading to TLE.

```py
d, i = heappop(pq)
if d > dis[i]:
    continue  # stale entry, skip
```

### Grid Problems
For grid-based Dijkstra, represent state as (cost, x, y) and use 4 or 8 directional offsets.

### Multiple Priorities (Tiebreaking)
For problems like LC 2146 (rank by price, then distance, then row, then col), use tuple comparison in the heap.

```py
heappush(pq, (distance, -price, row, col))  # negative for max-heap behavior
```

### Reverse Graph
When you need "shortest path TO node x from any other node," run Dijkstra on the reversed graph starting from x.

LC 2203 uses this for bidirectional shortest path problems.
