# Disjoint Set Union Template

``` py
# 1. path compression during 'find': find the root/cluster-id of u
# 2. union by rank, merge low rank set to high rank set: merge cluter x and cluster y
# 3. Time complexity of find and union is log(n)
class DSU:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        if self.p[x]!=x: self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)

# optional implementation
A = list(range(n+1))
def find(x):
    if A[x]!=x: A[x] = find(A[x])
    return A[x]

def union(x, y):
    A[find(x)] = find(y)

for x, y, v in roads:
    union(x, y)

dsu = DSU(`length`)
for i in range(n):
    `Condition`
    dsu.union(`x`, `y`)
return len(set([dsu.find(i) for i in range(len(dsu.p))])) # number of connected component
```

## Reference

1. [https://www.cs.princeton.edu/~rs/AlgsDS07/01UnionFind.pdf](https://www.cs.princeton.edu/~rs/AlgsDS07/01UnionFind.pdf)
