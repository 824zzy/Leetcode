# Graph Template

## Breadth First Search(BFS)

[Go to BFS template](./BFS/README.md)

## Depth First Search(DFS)

[Go to DFS template](./DFS/README.md)

## Shortest Path

TODO: refine template

1. Dijstra Algorithm

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

2. Floyd algorithm

``` py
def findTheCity(self, n, edges, maxd):
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
    return res[min(res)]
```
