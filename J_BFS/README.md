# Graph Template

## Breadth First Search(BFS)

In Q, it maybe also stores steps and other information.
When we have to build a graph by ourself, don't forget try to reduce time complexity by some tricks.

```py
def graghBFS(self, A: List[List[int]]) -> int:
    Q = [STATE_STATE]
    seen = set()
    while Q:
        i = Q.pop(0)
        if i not in seen:
            seen.add(i)
            for NEXT_STATES:
                if CONDITION:
                    Q.append(NEXT_STATE)
```

## Dijkstra Algorithm for Single-Source Shortest Paths

Difference between BFS and Dijkstra:

- Breadth-first search is just Dijkstra's algorithm with all edge weights equal to 1.
- Dijkstra's algorithm is conceptually breadth-first search that respects edge costs by heap.

Difference between Dijkstra and Floyd-Warshall algorithm

- Dijkstra's Algorithm is one example of a single-source shortest or SSSP algorithm, i.e., given a source vertex it finds shortest path from source to all other vertices.
- Floyd Warshall Algorithm is an example of all-pairs shortest path algorithm, meaning it computes the shortest path between all pair of nodes.

``` py
# time complexity O(E*logV)
G = collections.defaultdict(dict)
for i, j, w in edges: G[i][j] = w

pq = [(0, src)]
seen = {}
while pq:
    cost, i = heapq.heappop(pq)
    if i not in seen:
        seen[i] = cost
        for j in G[i]:
            heapq.heappush(pq, (cost+G[i][j], j))
# shortest path from src to all the nodes
shortest_paths = [seen.get(i, float("inf")) for i in range(n)]
```

### Floyd-Warshall Algorithm for All Pairs Shortest Paths

``` py
N = len(G)
# floyd-warshall
dist = [[inf]*N for _ in range(N)]
for i, x in enumerate(G):
    dist[i][i] = 0
    for j in x: dist[i][j] = 1
# or if edges are (i, j, w)
dist = [[float('inf')] * n for _ in range(n)]
for i, j, w in edges: dist[i][j] = dist[j][i] = w
for i in range(n): dist[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
```
