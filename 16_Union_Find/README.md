# Disjoint Set Union Template

``` py
class DSU:
    def __init__(self, n):
        self.p = [i for i in range(n)]
    def find(self, u):
        if self.p[u]!=u:
            self.p[u] = self.find(self.p[u])
        return self.p[u]
    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)

# Body
dsu = DSU(`length`)
for i in range(n):
    `Condition`
    dsu.merge(`x`, `y`)
return len(set([dsu.find(i) for i in range(len(dsu.p))]))
```
