# Graph Template

## Breadth First Search(BFS)

In Q, it maybe also stores steps and other information.
When we have to build a graph by ourself, don't forget try to reduce time complexity by some tricks.

```py
class Solution:
    def graghBFS(self, A: List[List[int]]) -> int:
        Q = ["start_state"]
        seen = set()
        while Q:
            i = Q.pop(0)
            if/for "logic":
                "logic to find next state j"
                if j not in seen:
                    Q.append(j)
                    seen.add(j)
        return ans
```

## Shortest Path

### Dijkstra Algorithm

Difference between BFS and Dijkstra:

- Breadth-first search is just Dijkstra's algorithm with all edge weights equal to 1.
- Dijkstra's algorithm is conceptually breadth-first search that respects edge costs.

TODO: refine template below

``` py
def dijkstra(self, times: List[List[int]], n: int, k: int) -> int:
    e = collections.defaultdict(dict)
    for i, j, d in times: e[i][j] = d
    pq = [(0, k)]
    seen = {}
    while pq:
        delay, i = heapq.heappop(pq)
        if i not in seen:
            seen[i] = delay
            for j in e[i]:
                delay2 = delay+e[i][j]
                if j not in seen:
                    heapq.heappush(pq, (delay2, j))
    if len(seen)!=n: return -1
    else: return max(seen.values())
```

### Floyd-Warshall algorithm

``` py
N = len(G)
# floyd-warshall
dist = [[inf]*N for _ in range(N)]
for i, x in enumerate(G):
    dist[i][i] = 0
    for j in x: dist[i][j] = 1
        
for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])


dis = [[float('inf')] * n for _ in xrange(n)]
for i, j, w in edges:
    dis[i][j] = dis[j][i] = w
for i in xrange(n):
    dis[i][i] = 0
for k in xrange(n):
    for i in xrange(n):
        for j in xrange(n):
            dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
res = {sum(d <= maxd for d in dis[i]): i for i in xrange(n)}
```
