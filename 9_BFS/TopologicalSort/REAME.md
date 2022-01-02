# Topological sort

## Template

``` py
def topological_sort(self, n: int, A: List[List[int]]) -> bool:
    e = defaultdict(list)
    inD = [0] * n
    for i, j in A:
        e[j].append(i)
        inD[i] += 1
    
    Q = [i for i, d in enumerate(inD) if d==0]
    while Q:
        i = Q.pop(0)
        for j in e[i]:
            inD[j] -= 1
            if not inD[j]: Q.append(j)
```