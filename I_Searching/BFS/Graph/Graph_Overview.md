---
tags:
  - leetcode
  - searching
  - moc
---

# BFS (Breadth-First Search)

## When to Use

| Problem Signal | Technique |
|---|---|
| Shortest path in unweighted graph | Standard BFS |
| Shortest path in matrix (4/8 directions) | Matrix BFS |
| Level-order traversal / distance from multiple sources | Multi-source BFS |
| Shortest path with 0/1 edge weights | 0-1 BFS (deque) |
| Shortest path with positive weights | Dijkstra (priority queue) |
| Connected components / flood fill | BFS or DFS (either works) |
| Shortest transformation sequence (word ladder, etc.) | BFS on implicit graph |
| State space exploration (puzzle, game) | BFS with state tuple |
| Minimum steps with constraints (k obstacles, alternating colors) | BFS with extended state |

## Standard BFS (Unweighted Graph)

Finds shortest path in unweighted graphs. O(V + E) time.

### Template: Adjacency list

```py
G = defaultdict(list)
for u, v in edges:
    G[u].append(v)
    G[v].append(u)

Q = [start]
seen = {start}
step = 0
while Q:
    for _ in range(len(Q)):
        node = Q.pop(0)
        if node == target:
            return step
        for nei in G[node]:
            if nei not in seen:
                seen.add(nei)
                Q.append(nei)
    step += 1
return -1
```

### Common patterns

**Count connected components:**

```py
G = defaultdict(list)
for u, v in edges:
    G[u].append(v)
    G[v].append(u)

seen = set()
def bfs(start):
    Q = [start]
    seen.add(start)
    while Q:
        node = Q.pop(0)
        for nei in G[node]:
            if nei not in seen:
                seen.add(nei)
                Q.append(nei)

ans = 0
for node in range(n):
    if node not in seen:
        bfs(node)
        ans += 1
return ans
```

**Track parent for path reconstruction:**

```py
Q = [start]
seen = {start}
parent = {start: None}
while Q:
    node = Q.pop(0)
    if node == target:
        break
    for nei in G[node]:
        if nei not in seen:
            seen.add(nei)
            parent[nei] = node
            Q.append(nei)

# reconstruct path
path = []
node = target
while node is not None:
    path.append(node)
    node = parent[node]
path.reverse()
```

### LC References

**Basic:** 797 (all paths), 1971 (path exists), 547 (provinces), 841 (keys and rooms), 1376 (time to inform), 582 (kill process), 2368 (reachable nodes), 3243 (shortest distance after queries)

**Shortest path / transformation:** 752 (open lock), 127 (word ladder), 433 (genetic mutation), 1197 (knight moves), 2059 (convert number), 1306 (jump game III), 1345 (jump game IV), 773 (sliding puzzle), 909 (snakes and ladders)

**Bipartite / two-color:** Use BFS to paint nodes, check for conflicts. LC 785

**Directed graph (in/out edges):** 1466 (reorder routes) - track edge direction with boolean flag

## Matrix BFS

Treat grid cells as graph nodes. 4-directional or 8-directional movement.

### Template: Standard matrix BFS

```py
m, n = len(A), len(A[0])
D = [(0, 1), (0, -1), (1, 0), (-1, 0)]

Q = [(start_x, start_y)]
seen = {(start_x, start_y)}
step = 0
while Q:
    for _ in range(len(Q)):
        x, y = Q.pop(0)
        if x == target_x and y == target_y:
            return step
        for dx, dy in D:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in seen and A[nx][ny] != obstacle:
                seen.add((nx, ny))
                Q.append((nx, ny))
    step += 1
return -1
```

### Template: Flood fill (modify in-place)

No need for separate `seen` set if you can mark visited cells in the grid.

```py
m, n = len(A), len(A[0])
D = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(x, y):
    Q = [(x, y)]
    A[x][y] = new_value  # mark visited
    while Q:
        x, y = Q.pop(0)
        for dx, dy in D:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and A[nx][ny] == old_value:
                A[nx][ny] = new_value
                Q.append((nx, ny))

for i in range(m):
    for j in range(n):
        if A[i][j] == target_value:
            bfs(i, j)
```

### LC References

**Flood fill / count components:** 200 (islands), 733 (flood fill), 695 (max area), 1905 (sub islands), 1254 (closed islands), 1020 (enclaves), 130 (surrounded regions), 417 (pacific atlantic), 1992 (farmland), 2658 (max fish)

**Shortest path:** 1926 (nearest exit), 1091 (shortest path in binary matrix), 490 (the maze)

**State tracking:** 529 (minesweeper), 2596 (knight tour), 2257 (unguarded cells)

## Multi-Source BFS

Start BFS from multiple sources at once. All sources are at distance 0. Useful for "distance to nearest X" problems.

### Template

```py
# collect all sources
Q = [(x, y) for x in range(m) for y in range(n) if A[x][y] == source_value]
seen = set(Q)

step = 0
while Q:
    for _ in range(len(Q)):
        x, y = Q.pop(0)
        for dx, dy in D:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in seen:
                seen.add((nx, ny))
                Q.append((nx, ny))
                # process (nx, ny) with distance = step + 1
    step += 1
```

### Key insight

Think of it as "flood outward from all sources simultaneously." The first time you reach a cell is the shortest distance from any source.

### LC References

**Distance to nearest:** 542 (01 matrix), 1162 (as far from land), 286 (walls and gates), 317 (shortest distance from all buildings)

**Spread / infection:** 994 (rotting oranges), 2385 (infected tree)

**Bridge between components:** 934 (shortest bridge) - DFS to find first island, then multi-source BFS from all cells of that island

## 0-1 BFS

For graphs where edges have weight 0 or 1. Use deque instead of queue: add 0-weight edges to front, 1-weight edges to back. O(V + E) time, faster than Dijkstra's O((V + E) log V).

### Template

```py
Q = deque([start])
dist = {start: 0}
while Q:
    node = Q.popleft()
    for nei, weight in G[node]:
        new_dist = dist[node] + weight
        if nei not in dist or new_dist < dist[nei]:
            dist[nei] = new_dist
            if weight == 0:
                Q.appendleft(nei)  # 0-weight: front
            else:
                Q.append(nei)      # 1-weight: back
return dist[target]
```

### When to recognize

- "minimum cost" where each edge has cost 0 or 1
- "shortest path with at most k obstacles" (treat obstacle crossing as weight 1)
- "alternating colors" (treat color change as weight 1)

### LC References

**0-1 edges:** 1293 (obstacles elimination) - can cross obstacle (cost 1) or not (cost 0)

**Alternating constraint:** 1129 (alternating colors) - color change is implicit cost

## Dijkstra (Priority Queue BFS)

For shortest path in weighted graphs with non-negative weights. O((V + E) log V) time.

### Template

```py
dist = {start: 0}
pq = [(0, start)]  # (cost, node)
while pq:
    cost, node = heappop(pq)
    if cost > dist.get(node, inf):
        continue  # already processed with better cost
    if node == target:
        return cost
    for nei, weight in G[node]:
        new_cost = cost + weight
        if new_cost < dist.get(nei, inf):
            dist[nei] = new_cost
            heappush(pq, (new_cost, nei))
return dist.get(target, -1)
```

### Common patterns

**Matrix with varying costs:**

```py
pq = [(0, start_x, start_y)]
dist = {(start_x, start_y): 0}
while pq:
    cost, x, y = heappop(pq)
    if (x, y) == (target_x, target_y):
        return cost
    for dx, dy in D:
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n:
            new_cost = cost + edge_weight(x, y, nx, ny)
            if new_cost < dist.get((nx, ny), inf):
                dist[(nx, ny)] = new_cost
                heappush(pq, (new_cost, nx, ny))
```

### LC References

**Weighted path:** 1631 (minimum effort) - edge weight is height difference, 778 (swim in rising water) - edge weight based on max height

**Multi-criteria optimization:** 2039 (network idle time)

## BFS with Extended State

When you need to track more than just position (e.g., position + remaining quota, position + parity, position + parent direction).

### Template

```py
# state = (x, y, extra_info)
Q = [(start_x, start_y, start_extra)]
seen = {(start_x, start_y, start_extra)}
step = 0
while Q:
    for _ in range(len(Q)):
        x, y, extra = Q.pop(0)
        if is_target(x, y, extra):
            return step
        for nx, ny, new_extra in get_neighbors(x, y, extra):
            if (nx, ny, new_extra) not in seen:
                seen.add((nx, ny, new_extra))
                Q.append((nx, ny, new_extra))
    step += 1
return -1
```

### Common state extensions

**Remaining quota:** (x, y, k) where k = obstacles remaining to eliminate
- LC 1293 (obstacles elimination)

**Parity / modulo:** (x, y, balance % 2) for parentheses matching
- LC 2267 (valid parentheses path)

**Direction / color:** (x, y, last_color) for alternating constraints
- LC 1129 (alternating colors)

## Binary Search + BFS

For "minimum capacity to reach target" or "minimum threshold for feasibility" problems. Binary search on answer, use BFS to check feasibility.

### Template

```py
def feasible(threshold):
    # BFS to check if target is reachable under threshold constraint
    Q = [start]
    seen = {start}
    while Q:
        node = Q.pop(0)
        if node == target:
            return True
        for nei in G[node]:
            if edge_satisfies_threshold(node, nei, threshold) and nei not in seen:
                seen.add(nei)
                Q.append(nei)
    return False

l, r = min_possible, max_possible
while l < r:
    m = (l + r) // 2
    if feasible(m):
        r = m
    else:
        l = m + 1
return l
```

### LC References

1631 (minimum effort), 778 (swim in rising water) - both can be solved with binary search + BFS or Dijkstra

## DFS vs BFS Decision

| Use DFS when | Use BFS when |
|---|---|
| Any path works (not shortest) | Need shortest path (unweighted) |
| Exploring all possibilities (backtracking) | Level-order traversal matters |
| Need full path before deciding (path validation) | Distance from source matters |
| Implicit recursion is cleaner | Iterative is required (Python recursion limit) |
| Memory is tight (DFS uses call stack) | All neighbors must be explored first |

**Either works:** Connected components, flood fill, cycle detection, topological sort (DFS cleaner for topo sort)

## Implementation Notes

**Queue choice:**
- `Q.pop(0)` - simple but O(n) per pop
- `collections.deque` with `popleft()` - O(1) per pop, preferred for large queues
- Level-by-level: `for _ in range(len(Q))` to process one level at a time

**Seen set timing:**
- Add to `seen` when adding to queue (not when popping) to avoid duplicates in queue
- Exception: if you need to update with better cost (Dijkstra-style), check on pop

**In-place marking:**
- If grid is mutable and you won't need original values, mark visited cells directly (e.g., `A[x][y] = -1`)
- Saves space, no separate `seen` set needed

**Direction vectors:**
- 4-directional: `D = [(0,1), (0,-1), (1,0), (-1,0)]`
- 8-directional: add diagonals `[(1,1), (1,-1), (-1,1), (-1,-1)]`
- Knight moves: `D = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]`

## Common Mistakes

1. **Not marking as seen when adding to queue** - leads to duplicates and TLE
2. **Checking target in wrong place** - check when adding to queue (not when popping) for true shortest distance
3. **Mutable default argument** - don't use `def bfs(seen=set())`, create fresh set inside
4. **Incorrect level tracking** - use `for _ in range(len(Q))` to process one level at a time
5. **Forgetting boundary checks** - always check `0 <= x < m and 0 <= y < n` before accessing `A[x][y]`

## Complexity Reference

| Graph Type | V | E | BFS Time | BFS Space |
|---|---|---|---|---|
| Adjacency list | V | E | O(V + E) | O(V) |
| Matrix m×n | mn | ~4mn | O(mn) | O(mn) |
| Implicit (state space) | V | E | O(V + E) | O(V) |

Dijkstra: O((V + E) log V) time, O(V) space
