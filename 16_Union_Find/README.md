# Disjoint Set Union Template

``` py
# 1. path compression during 'find': find the root/cluster-id of u
# 2. union by rank, merge low rank set to high rank set: merge cluter x and cluster y
class DSU:
    def __init__(self, n):
        self.p = [i for i in range(n)]

    def find(self, x1):
        if self.p[x]!=x: self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)

dsu = DSU(`length`)
for i in range(n):
    `Condition`
    dsu.union(`x`, `y`)
return len(set([dsu.find(i) for i in range(len(dsu.p))])) # number of connected component
```

## Reference

1. [https://www.cs.princeton.edu/~rs/AlgsDS07/01UnionFind.pdf](https://www.cs.princeton.edu/~rs/AlgsDS07/01UnionFind.pdf)
