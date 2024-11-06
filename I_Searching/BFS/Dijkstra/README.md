# Dijkstra Algorithm for Single-Source Shortest Paths

Difference between BFS and Dijkstra:

- Breadth-first search is just Dijkstra's algorithm with all edge weights equal to 1.
- Dijkstra's algorithm is conceptually breadth-first search that respects edge costs by heap.

Difference between Dijkstra and Floyd-Warshall algorithm

- Dijkstra's Algorithm is one example of a single-source shortest or SSSP algorithm, i.e., given a source vertex it finds shortest path from source to all other vertices.
- Floyd Warshall Algorithm is an example of all-pairs shortest path algorithm, meaning it computes the shortest path between all pair of nodes.

``` py
# time complexity O(E*logV)
G = [[] for _ in range(n+1)]
for i, j, w in A:
    G[i].append((j, w))

pq = [(0, k)]
dis = [inf]*(n+1)
# init dis
while pq:
    d, i = heappop(pq)
    if d>dis[i]:
        continue
    for j, w in G[i]:
        new_d = d+w
        if new_d<dis[j]:
            dis[j] = new_d
            heappush(pq, (new_d, j))
```