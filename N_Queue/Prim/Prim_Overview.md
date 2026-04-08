---
tags:
  - leetcode
  - queue
  - moc
---

# Prim's Algorithm

## When to Use

Prim's algorithm builds a minimum spanning tree (MST) by greedily adding the cheapest edge that connects a new vertex to the growing tree. Use when you need to connect all nodes with minimum total edge cost.

| Problem Signal | Use Prim | Use Kruskal |
|---|---|---|
| Dense graph (E ≈ V²) | ✓ Better | Works but slower |
| Sparse graph (E ≈ V) | Works | ✓ Better |
| Need MST starting from specific vertex | ✓ Natural fit | Possible but awkward |
| Edges given as adjacency list | ✓ Natural fit | Need to extract edges |
| Edges given as sorted edge list | Possible | ✓ Natural fit |
| Need to track tree construction order | ✓ Natural | Harder |
| Online algorithm (add vertices incrementally) | ✓ Yes | No |

**Complexity:** O(E log V) with heap. For complete graphs (all pairs connected), E = V², so O(V² log V).

## Core Template

```py
G = defaultdict(dict)
for i in range(len(A)):
    for j in range(i+1, len(A)):
        dist = COMPUTE_DIST(A[i], A[j])
        G[i][j] = dist
        G[j][i] = dist

seen = set()
minHeap = [[0, 0]]  # (cost, vertex), start from vertex 0 with cost 0
total_cost = 0
while len(seen) < len(A):
    cost, u = heappop(minHeap)
    if u in seen: continue
    seen.add(u)
    total_cost += cost
    for v, d in G[u].items():
        if v not in seen:
            heappush(minHeap, [d, v])
return total_cost
```

## Key Insights

1. **Greedy is optimal:** Always pick the cheapest edge to expand the tree. This works because MST has the cut property (the minimum edge crossing any cut is in some MST).

2. **Heap invariant:** The heap contains all edges from visited nodes to unvisited nodes. We always pick the minimum.

3. **Visited check is critical:** When you pop `(cost, u)` from the heap, check if `u` is already visited. If yes, skip it. This handles duplicate entries in the heap.

4. **Starting vertex doesn't matter:** MST cost is the same regardless of which vertex you start from. But if the problem asks for a specific root (rare), start from that vertex.

5. **Disconnected graphs:** If the graph is disconnected, this template will loop forever (or until heap is empty). Check `len(seen) == n` after the loop to detect this.

## Variants

### Track parent pointers (tree structure)

Some problems need to know the actual MST edges, not just the cost.

```py
parent = {}
minHeap = [[0, 0, -1]]  # (cost, vertex, parent)
while len(seen) < n:
    cost, u, p = heappop(minHeap)
    if u in seen: continue
    seen.add(u)
    parent[u] = p  # record edge (p, u) is in MST
    total_cost += cost
    for v, d in G[u].items():
        if v not in seen:
            heappush(minHeap, [d, v, u])
```

### Start from specific vertex (rooted MST)

Just change the initial heap entry.

```py
minHeap = [[0, start_vertex]]
```

### Track number of edges added

Useful for checking if MST exists (should have exactly n-1 edges).

```py
edges_added = 0
while minHeap and edges_added < n - 1:
    cost, u = heappop(minHeap)
    if u in seen: continue
    seen.add(u)
    total_cost += cost
    edges_added += 1
    for v, d in G[u].items():
        if v not in seen:
            heappush(minHeap, [d, v])
return total_cost if edges_added == n - 1 else -1  # -1 if disconnected
```

## Complexity Analysis

**Time:** O(E log V)
- Each edge is added to the heap at most once: O(E) heap insertions.
- Each heap pop is O(log V).
- Total: O(E log V).
- For complete graphs (E = V²), this becomes O(V² log V).

**Space:** O(E + V)
- Graph storage: O(E)
- Heap: O(E) in worst case
- Seen set: O(V)

## Comparison: Prim vs Kruskal

Both solve MST. Choose based on input format and graph density.

| Aspect | Prim | Kruskal |
|---|---|---|
| **Algorithm** | Grow tree from one vertex | Sort all edges, union vertices |
| **Data structures** | Min heap, adjacency list | Sorted edge list, union-find |
| **Complexity** | O(E log V) | O(E log E) = O(E log V) |
| **Dense graph (E ≈ V²)** | Better constant factors | Sorting overhead |
| **Sparse graph (E ≈ V)** | Similar | Similar |
| **Input: adjacency list** | Natural | Need to extract edges |
| **Input: edge list** | Build graph first | Natural |
| **Start from specific vertex** | Easy | Hard |
| **Online (add vertices)** | Yes | No |

## LeetCode Problems

| Problem | Difficulty | Notes |
|---|---|---|
| [1584. Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) | L1 | Classic MST, Manhattan distance |

## Common Pitfalls

1. **Forgetting visited check after heap pop:** You'll add edges multiple times and get wrong answer or TLE.
   ```py
   # WRONG
   cost, u = heappop(minHeap)
   seen.add(u)  # should check first!
   ```

2. **Adding visited nodes to heap:** Not wrong, but wasteful. The `if v not in seen` check before pushing saves space and time.

3. **Wrong graph construction:** For undirected graphs, add edge in both directions. For directed graphs, Prim doesn't apply (MST is for undirected graphs only).

4. **Off-by-one in edge count:** MST has exactly n-1 edges. If you count n edges, something went wrong.

5. **Not handling disconnected graphs:** If the graph has multiple components, Prim will only find the MST of one component. Check `len(seen) == n` after the loop.

## Related Algorithms

- **Kruskal's algorithm:** Alternative MST algorithm using union-find. See `P_UnionFind/Kruskal/`.
- **Dijkstra's algorithm:** Shortest path from single source. Similar heap structure but tracks distance from source, not edge cost. See `I_Searching/BFS/Dijkstra/`.
- **Borůvka's algorithm:** Another MST algorithm, useful for parallel computation. Not common in competitive programming.

## Reference

- [Python: Kruskal & Prim - Standard code - Clean & Concise](https://leetcode.com/problems/min-cost-to-connect-all-points/discuss/1476951/Python-2-solutions%3A-Kruskal-and-Prim-Standard-code-Clean-and-Concise)
