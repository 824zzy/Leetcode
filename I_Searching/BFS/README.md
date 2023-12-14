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

### Floyd-Warshall Algorithm for All Pairs Shortest Paths

``` py
N = len(G)
# floyd-warshall
dist = [[inf]*N for _ in range(N)]
for i, x in enumerate(G):
    dist[i][i] = 0
    for j in x: dist[i][j] = 1
# or if edges are (i, j, w)
dist = [[inf] * n for _ in range(n)]
for i, j, w in edges: dist[i][j] = dist[j][i] = w
for i in range(n): dist[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```
