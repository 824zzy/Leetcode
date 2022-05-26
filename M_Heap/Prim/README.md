# Prim's Algorithm

Prim's algorithm start to build the minimum spanning tree from minimum weighted vertex in the graph.

Time complexity: O(ElogV) ~= O(N^2logN)

## Template

``` py
G = defaultdict(dict)
for i in range(len(A)):
    for j in range(i+1, len(A)):
        COMPUTE DIST
        G[i][j] = dist
        G[j][i] = dist

seen = set()
minHeap = [[0, 0]]  # pair of (dist, vertex)
total_dist = 0
while len(seen)<len(A):
    dist, u = heappop(minHeap)
    if u in seen: continue
    seen.add(u)
    total_dist += dist
    for v, d in G[u].items():
        if v not in seen:
            heappush(minHeap, [d, v])
return total_dist
```

## Reference

- [[Python] 2 solutions: Kruskal & Prim - Standard code - Clean & Concise](https://leetcode.com/problems/min-cost-to-connect-all-points/discuss/1476951/Python-2-solutions%3A-Kruskal-and-Prim-Standard-code-Clean-and-Concise)
