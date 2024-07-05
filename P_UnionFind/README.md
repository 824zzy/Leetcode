# Disjoint Set / Union-Find

Disjoint Set Union a disjoint-set data structure, also called a union–find data structure or merge–find set, is a data structure that stores a collection of disjoint (non-overlapping) sets. There are several key points in the implementation of the disjoint set union data structure:
1. path compression during 'find': find the root/cluster-id of u
2. union by rank, merge low rank set to high rank set: merge cluster x and cluster y
3. Time complexity of find and union is log(n)

## Template 

Array-Based Implementation
``` py
A = list(range(n+1))
def find(x):
    if A[x]!=x: A[x] = find(A[x])
    return A[x]
def union(x, y):
    A[find(x)] = find(y)

def union(x, y):
    # when x and y are in the same cluster, return False
    xx, yy = find(x), find(y)
    if xx==yy: return False
    A[xx] = yy
    return True
```

Dictionary-Based Implementation
``` py
dsu = {}
def find(x):
    if x not in dsu: dsu[x] = x
    elif dsu[x]!=x: dsu[x] = find(dsu[x])
    return dsu[x]

def union(x, y):
    dsu[find(x)] = find(y)

def union(x, y):
    # when x and y are in the same cluster, return False
    xx, yy = find(x), find(y)
    if xx==yy: return False
    dsu[xx] = yy
    return True
```

## Application: Kruskal's Algorithm

Kruskal's algorithm start to build the minimum spanning tree from minimum weighted vertex in the graph.
Time complexity: O(ElogV) ~= O(N^2logN)

Kruskal's Algorithm Template:

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
1. [https://www.cs.princeton.edu/~rs/AlgsDS07/01UnionFind.pdf](https://www.cs.princeton.edu/~rs/AlgsDS07/01UnionFind.pdf)
