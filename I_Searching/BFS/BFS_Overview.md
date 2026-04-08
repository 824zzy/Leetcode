---
tags:
  - leetcode
  - searching
  - moc
---

# Breadth First Search (BFS)

## When to Use

| Problem Signal | Technique |
|---|---|
| Shortest path in unweighted graph | Standard BFS |
| Level-by-level exploration (tree, graph) | Level-order BFS |
| Multiple sources spreading simultaneously | Multi-source BFS |
| Need distance from all nodes to a target | Reverse BFS (from target) |
| Shortest path meets from both ends | Bidirectional BFS |
| Need to track path or reconstruct solution | BFS with parent pointers |
| State space exploration (word ladder, sliding puzzle) | BFS on implicit graph |
| Shortest path with obstacles you can remove | BFS with extended state (pos, remaining_removes) |
| Graph with cycles, need visited tracking | BFS with seen set |
| Matrix connectivity / flood fill | Grid BFS with 4/8 directions |

## Standard BFS (Graph)

Use when you need shortest path in unweighted graph or level-by-level exploration.

LC 1971, 797, 841, 200, 547, 1376, 127

```py
def bfs(start):
    Q = [start]
    seen = {start}
    while Q:
        node = Q.pop(0)
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                Q.append(neighbor)
```

## Level-Order BFS (with Step Tracking)

Use when you need to track distance/level or process nodes level by level.

LC 127, 1197, 1926, 286, 994

```py
def bfs_with_steps(start):
    Q = [start]
    seen = {start}
    step = 0
    while Q:
        for _ in range(len(Q)):
            node = Q.pop(0)
            if is_target(node):
                return step
            for neighbor in get_neighbors(node):
                if neighbor not in seen:
                    seen.add(neighbor)
                    Q.append(neighbor)
        step += 1
    return -1  # target not found
```

## Multi-Source BFS

Use when multiple sources spread simultaneously (e.g., all rotten oranges, all gates).

LC 994, 286, 1765

**Key insight:** Initialize queue with all sources at step 0. The BFS naturally finds the minimum distance from any source to each cell.

```py
def multi_source_bfs(grid, sources):
    m, n = len(grid), len(grid[0])
    Q = list(sources)  # all starting points
    seen = set(sources)
    step = 0

    while Q:
        for _ in range(len(Q)):
            x, y = Q.pop(0)
            for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in seen:
                    if is_valid(grid[nx][ny]):
                        seen.add((nx, ny))
                        Q.append((nx, ny))
        step += 1
    return step
```

## Bidirectional BFS

Use when you know both start and end, and want to optimize search (meet in the middle).

LC 127, 752

**Key insight:** Search from both ends simultaneously. Stop when the two frontiers meet. Can reduce time from O(b^d) to O(b^(d/2)).

```py
def bidirectional_bfs(start, end):
    if start == end:
        return 0

    front = {start}
    back = {end}
    seen_front = {start}
    seen_back = {end}
    step = 0

    while front and back:
        # always expand smaller frontier
        if len(front) > len(back):
            front, back = back, front
            seen_front, seen_back = seen_back, seen_front

        next_front = set()
        for node in front:
            for neighbor in get_neighbors(node):
                if neighbor in back:
                    return step + 1
                if neighbor not in seen_front:
                    seen_front.add(neighbor)
                    next_front.add(neighbor)
        front = next_front
        step += 1

    return -1
```

## Grid BFS (Matrix)

Use for matrix connectivity, flood fill, shortest path in grid.

LC 200, 695, 733, 1926, 490, 994, 286

```py
def grid_bfs(grid, start_x, start_y):
    m, n = len(grid), len(grid[0])
    Q = [(start_x, start_y)]
    grid[start_x][start_y] = visited_marker

    while Q:
        x, y = Q.pop(0)
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == target:
                grid[nx][ny] = visited_marker
                Q.append((nx, ny))
```

### 8-directional movement

For problems where diagonal movement is allowed:

```py
D8 = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
```

## BFS with State Tracking

Use when state is more than just position (e.g., position + keys collected, position + obstacles removed).

LC 864, 1293, 847

```py
def bfs_with_state(start_state):
    Q = [start_state]
    seen = {start_state}
    step = 0

    while Q:
        for _ in range(len(Q)):
            state = Q.pop(0)
            if is_goal(state):
                return step
            for next_state in get_next_states(state):
                if next_state not in seen:
                    seen.add(next_state)
                    Q.append(next_state)
        step += 1
    return -1
```

## Implicit Graph BFS (State Space Exploration)

Use for problems like word ladder, sliding puzzle, or any state transformation.

LC 127, 752, 773, 909

**Key insight:** Nodes are states (strings, board configurations), edges are valid transformations. Build graph on the fly.

```py
def state_space_bfs(start, target):
    Q = [(start, 0)]
    seen = {start}

    while Q:
        state, step = Q.pop(0)
        if state == target:
            return step

        # generate next states on the fly
        for next_state in get_valid_transformations(state):
            if next_state not in seen:
                seen.add(next_state)
                Q.append((next_state, step + 1))
    return -1
```

## BFS with Path Reconstruction

Use when you need to return the actual path, not just the distance.

LC 126, 127

```py
def bfs_with_path(start, target):
    Q = [(start, [start])]
    seen = {start}

    while Q:
        node, path = Q.pop(0)
        if node == target:
            return path

        for neighbor in get_neighbors(node):
            if neighbor not in seen:
                seen.add(neighbor)
                Q.append((neighbor, path + [neighbor]))
    return []
```

For multiple shortest paths (LC 126), track all parents at each level:

```py
def bfs_all_shortest_paths(start, target):
    Q = [start]
    parent = defaultdict(list)
    seen = {start}
    found = False

    while Q and not found:
        next_Q = []
        # process entire level before adding to seen
        level_seen = set()
        for node in Q:
            if node == target:
                found = True
            for neighbor in get_neighbors(node):
                if neighbor not in seen:
                    parent[neighbor].append(node)
                    if neighbor not in level_seen:
                        level_seen.add(neighbor)
                        next_Q.append(neighbor)
        seen.update(level_seen)
        Q = next_Q

    # backtrack from target to start using parent pointers
    return reconstruct_all_paths(parent, start, target)
```

## Topological Sort (BFS / Kahn's Algorithm)

Use for dependency resolution, course scheduling, or any DAG ordering.

LC 207, 210, 1136, 2050, 802

**Key insight:** Start with nodes that have no incoming edges (in-degree 0). As you process each node, decrement in-degrees of neighbors. Add to queue when in-degree becomes 0.

```py
def topological_sort_bfs(n, edges):
    graph = defaultdict(list)
    in_degree = [0] * n

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    Q = [i for i in range(n) if in_degree[i] == 0]
    result = []

    while Q:
        node = Q.pop(0)
        result.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                Q.append(neighbor)

    # if len(result) < n, there's a cycle
    return result if len(result) == n else []
```

## 0-1 BFS (Weighted Graph with 0/1 Weights)

Use for shortest path when edge weights are only 0 or 1. Faster than Dijkstra.

**Key insight:** Use deque. Add 0-weight edges to front, 1-weight edges to back. Maintains sorted order.

```py
from collections import deque

def bfs_01(start, n, graph):
    dist = [inf] * n
    dist[start] = 0
    Q = deque([start])

    while Q:
        node = Q.popleft()
        for neighbor, weight in graph[node]:
            new_dist = dist[node] + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                if weight == 0:
                    Q.appendleft(neighbor)
                else:
                    Q.append(neighbor)

    return dist
```

## Key Insights

### When to use BFS vs DFS
- **BFS**: Shortest path, level-order traversal, minimum steps
- **DFS**: Path existence, connectivity, cycle detection, backtracking

### Visited tracking strategies
- **Modify input array**: Space O(1), mutates input (mark as visited with special value)
- **Separate seen set**: Space O(n), preserves input
- **Mark when adding to queue**: Prevents duplicates in queue (preferred)
- **Mark when popping from queue**: Allows revisiting if better path found (not typical for BFS)

### Graph construction optimization
For problems like word ladder (LC 127):
- **Don't** build full adjacency list with O(n²) comparisons
- **Do** generate candidates by trying all 26 letters at each position: O(n × len(word) × 26)

### Multi-source BFS trick
Initialize queue with all sources. No need for special handling—BFS naturally computes minimum distance from any source.

### Bidirectional BFS optimization
Always expand the smaller frontier. This keeps search balanced and maximizes the O(b^(d/2)) improvement.

### Common mistakes
- Forgetting to mark as seen when adding to queue (causes duplicate work)
- Using DFS when BFS is needed for shortest path
- Not handling the case where target is unreachable
- Off-by-one errors in step counting (check if you need steps before first level or after last level)
