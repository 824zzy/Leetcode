# Graph DFS template

## Type 1: Matrix

``` py
M, N = len(A), len(A[0])
D = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def dfs(x, y):
    LOGIC
    for dx, dy in D:
        if 0<=x+dx<M and 0<=y+dy<N and CONDITION:
            dfs(x+dx, y+dy)
    return STH

for i in range(M):
    for j in range(N):  
        dfs(i, j)
return ans
```

## Type2: Graph

``` py
G = defaultdict(dict)
for i in range(len(A)):
    for j in range(i+1, len(A)):
        if A[i][j]: G[i][j] = G[j][i] = 1
seen = set()

def dfs(i):
    seen.add(i)
    for j in G[i]:
        if j not in seen:
            dfs(j)
    
for i in range(len(A)):
    if i not in seen:
        dfs(i)
```
