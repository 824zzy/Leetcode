# Kruskal's Algorithm

Kruskal's algorithm start to build the minimum spanning tree from minimum weighted vertex in the graph.

Time complexity: O(ElogV) ~= O(N^2logN)

## Template

``` py
class DSU:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        if self.p[x]!=x: self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)
        
# find all edges and sort edges by distance
edges = []
for i in range(len(A)):
    for j in range(i+1, len(A)):
        COMPUTE DIST
        edges.append((dist, i, j))
edges.sort()

ans = 0
dsu = DSU(len(A))

for dist, i, j in edges:
    if dsu.find(i)!=dsu.find(j):
        dsu.union(i, j)
        ans += dist
return ans 
```

## Reference

- [[Python] 2 solutions: Kruskal & Prim - Standard code - Clean & Concise](https://leetcode.com/problems/min-cost-to-connect-all-points/discuss/1476951/Python-2-solutions%3A-Kruskal-and-Prim-Standard-code-Clean-and-Concise)