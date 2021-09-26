# Disjoint Set Union Template

TODO: check whether most of them are graph problem and merge them into graph category.

``` py
class DSU:
    """
    1. path compression during 'find'
    2. union by rank, merge low rank set to high rank set(not implement in template)
    """
    def __init__(self, n):
        self.p = [i for i in range(n)]

    def find(self, u):
        # find the root/cluster-id of u
        if self.p[u]!=u:
            self.p[u] = self.find(self.p[u])
        return self.p[u]

    def union(self, x, y):
        # merge cluter x and cluster y
        self.p[self.find(x)] = self.find(y)

# Body
dsu = DSU(`length`)
for i in range(n):
    `Condition`
    dsu.union(`x`, `y`)
return len(set([dsu.find(i) for i in range(len(dsu.p))])) # number of connected component
```

## Reference

1. [https://www.cs.princeton.edu/~rs/AlgsDS07/01UnionFind.pdf](https://www.cs.princeton.edu/~rs/AlgsDS07/01UnionFind.pdf)
