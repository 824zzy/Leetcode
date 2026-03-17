# Floyd-Warshall Algorithm

## When to Use

| Problem Signal | Use Floyd-Warshall |
|---|---|
| All-pairs shortest paths needed | ✓ |
| Graph fits in memory (n ≤ 500) | ✓ |
| Multiple shortest path queries | ✓ |
| Negative edge weights allowed (no negative cycles) | ✓ |
| Need transitive closure / reachability | ✓ |
| Single source shortest path | ✗ (use Dijkstra or Bellman-Ford) |
| Sparse graph with few queries | ✗ (use Dijkstra per query) |
| Graph is too large (n > 500) | ✗ (use Dijkstra or BFS) |

### Algorithm Selection

| Algorithm | Time | Space | Best For |
|---|---|---|---|
| Floyd-Warshall | O(n³) | O(n²) | All-pairs, dense graph, n ≤ 500, negative weights OK |
| Dijkstra (per query) | O(q · n log n) | O(n) | Few queries, sparse graph, no negative weights |
| Bellman-Ford | O(n · m) | O(n) | Single source, detect negative cycles, sparse graph |
| BFS (unweighted) | O(n + m) | O(n) | Unweighted graph, single/few sources |

## Core Template

```py
n = len(graph)
dist = [[inf] * n for _ in range(n)]

# initialize: self-loops are 0
for i in range(n):
    dist[i][i] = 0

# initialize: direct edges
for i, j, w in edges:
    dist[i][j] = w  # or min(dist[i][j], w) if multiple edges
    # dist[j][i] = w  # add this for undirected graph

# floyd-warshall
for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```

After running, `dist[i][j]` is the shortest path from i to j. If `dist[i][j] == inf`, there's no path.

## Variant Patterns

### Transitive Closure / Reachability

When you only care about reachability (not distance), use boolean logic instead of min/addition.

**LC 1462 (Course Schedule IV)**

```py
# initialize
reach = [[False] * n for _ in range(n)]
for i in range(n):
    reach[i][i] = True
for i, j in edges:
    reach[i][j] = True

# transitive closure
for k in range(n):
    for i in range(n):
        for j in range(n):
            reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
```

Or keep using `dist` with `inf` and check `dist[i][j] != inf`.

### Character/Symbol Graph (Small Domain)

When nodes are characters or small symbols, map them to integers 0..25 or 0..51.

**LC 2976 (Minimum Cost to Convert String I)**

```py
n = 26
dist = [[inf] * n for _ in range(n)]
for i in range(n):
    dist[i][i] = 0

# build graph from character edges
for s, t, w in zip(original, changed, cost):
    s, t = ord(s) - ord('a'), ord(t) - ord('a')
    dist[s][t] = min(dist[s][t], w)  # handle multiple edges

# floyd-warshall
for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# answer queries
for c1, c2 in queries:
    i, j = ord(c1) - ord('a'), ord(c2) - ord('a')
    cost = dist[i][j]  # inf if impossible
```

### Adjacency List Input

When graph is given as adjacency list (common in LC graph problems):

```py
N = len(graph)
dist = [[inf] * N for _ in range(N)]
for i in range(N):
    dist[i][i] = 0
    for j in graph[i]:
        dist[i][j] = 1  # unweighted

# floyd-warshall
for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```

### Floyd-Warshall + DP

Use Floyd-Warshall to preprocess all-pairs distances, then solve a DP problem that queries those distances.

**LC 847 (Shortest Path Visiting All Nodes)** - TSP-style bitmask DP on top of Floyd-Warshall distances:

```py
# step 1: floyd-warshall
dist = [[inf] * n for _ in range(n)]
for i, neighbors in enumerate(graph):
    dist[i][i] = 0
    for j in neighbors:
        dist[i][j] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# step 2: bitmask DP (TSP)
@cache
def dp(node, mask):
    if mask == 0:
        return 0
    ans = inf
    for next_node in range(n):
        if mask & (1 << next_node):
            ans = min(ans, dist[node][next_node] + dp(next_node, mask ^ (1 << next_node)))
    return ans

return min(dp(i, (1 << n) - 1) for i in range(n))
```

## Common Use Cases

1. **Find city with fewest neighbors within threshold** (LC 1334)
   - Run Floyd-Warshall, then count `dist[i][j] <= threshold` for each city

2. **Check if course A is prerequisite of course B** (LC 1462)
   - Transitive closure variant

3. **Character transformation with minimum cost** (LC 2976)
   - Small domain (26 letters) makes O(n³) = O(17k) very fast

4. **TSP / Hamiltonian path with preprocessing** (LC 847)
   - Floyd-Warshall + bitmask DP

5. **Multiple shortest path queries on dense graph**
   - Better than running Dijkstra q times when q is large and graph is dense

## Key Insights

1. **Loop order matters**: k must be the outermost loop. This ensures that when considering paths through k, all paths using intermediate nodes < k are already optimal.

2. **Self-loops**: Always set `dist[i][i] = 0` before the algorithm runs. Don't rely on the min operation to do it.

3. **Multiple edges**: If there can be multiple edges between the same pair of nodes, use `dist[i][j] = min(dist[i][j], w)` during initialization.

4. **Space optimization**: Floyd-Warshall modifies the distance matrix in-place. No auxiliary space needed beyond the O(n²) distance matrix.

5. **Time complexity**: Always O(n³). Independent of edge count. Works well on dense graphs (m ≈ n²) but wasteful on sparse graphs.

6. **Negative weights**: Floyd-Warshall handles negative edges correctly, as long as there are no negative cycles. To detect negative cycles, check if `dist[i][i] < 0` after the algorithm runs.

## LeetCode Problems

- [LC 1334 - Find the City With Smallest Number of Neighbors](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/) - All-pairs shortest paths, count neighbors
- [LC 1462 - Course Schedule IV](https://leetcode.com/problems/course-schedule-iv/) - Transitive closure / reachability
- [LC 2976 - Minimum Cost to Convert String I](https://leetcode.com/problems/minimum-cost-to-convert-string-i/) - Character graph, small domain
- [LC 847 - Shortest Path Visiting All Nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) - Floyd-Warshall + bitmask DP
- [LC 2959 - Number of Possible Sets of Closing Branches](https://leetcode.com/problems/number-of-possible-sets-of-closing-branches/) - Enumerate subsets, check connectivity

## Complexity

| Operation | Time | Space |
|---|---|---|
| Build distance matrix | O(n³) | O(n²) |
| Query shortest path | O(1) | - |
| Detect negative cycle | O(n) | - |
