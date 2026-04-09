# Topological sort

## Template

**Suppose that the edges are from i to j in A.**

``` py
def topological_sort(self, n: int, A: List[List[int]]) -> bool:
    G = defaultdict(list)
    inD = [0] * n
    for i, j in A:
        G[i].append(j)
        inD[j] += 1
    
    Q = [i for i, d in enumerate(inD) if d==0]
    while Q:
        i = Q.pop(0)
        for j in e[i]:
            inG[j] -= 1
            if not inD[j]: 
                Q.append(j)
```
