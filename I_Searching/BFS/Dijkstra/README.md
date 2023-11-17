# Dijkstra Algorithm for Single-Source Shortest Paths

Difference between BFS and Dijkstra:

- Breadth-first search is just Dijkstra's algorithm with all edge weights equal to 1.
- Dijkstra's algorithm is conceptually breadth-first search that respects edge costs by heap.

Difference between Dijkstra and Floyd-Warshall algorithm

- Dijkstra's Algorithm is one example of a single-source shortest or SSSP algorithm, i.e., given a source vertex it finds shortest path from source to all other vertices.
- Floyd Warshall Algorithm is an example of all-pairs shortest path algorithm, meaning it computes the shortest path between all pair of nodes.

``` py
# time complexity O(E*logV)
G = defaultdict(list)
for u, v, w in edges: 
    G[u].append((v, w))

pq = [(0, src)]
seen = {}
while pq:
    cost, i = heappop(pq)
    if i not in seen:
        seen[i] = cost
        for j in G[i]:
            heappush(pq, (cost+G[i][j], j))
# shortest path from src to all the nodes
shortest_paths = [seen.get(i, inf) for i in range(n)]
```

``` py
# time complexity O(E*logV)
G = defaultdict(list)
for u, v, w in edges: 
    G[u].append((v, w))

pq = [(0, src)]
seen = {src: 0}
while pq:
    cost, i = heappop(pq)
    for j in G[i]:
        if j not in seen or cost+G[i][j] < seen[j]:
            seen[j] = cost+G[i][j]
            heappush(pq, (cost+G[i][j], j))
# shortest path from src to all the nodes
shortest_paths = [seen.get(i, inf) for i in range(n)]
```