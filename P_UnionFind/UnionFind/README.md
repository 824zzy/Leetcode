# Disjoint Set Union Template

1. path compression during 'find': find the root/cluster-id of u
2. union by rank, merge low rank set to high rank set: merge cluster x and cluster y
3. Time complexity of find and union is log(n)

``` py
A = list(range(n+1))
def find(x):
    if A[x]!=x: A[x] = find(A[x])
    return A[x]
def union(x, y):
    A[find(x)] = find(y)

for x, y, v in roads:
    union(x, y)
```

``` py
dsu = {}
def find(x):
    if x not in dsu: dsu[x] = x
    elif dsu[x]!=x: dsu[x] = find(dsu[x])
    return dsu[x]

def union(x, y):
    dsu[find(x)] = find(y)
```

## Reference

1. [https://www.cs.princeton.edu/~rs/AlgsDS07/01UnionFind.pdf](https://www.cs.princeton.edu/~rs/AlgsDS07/01UnionFind.pdf)
