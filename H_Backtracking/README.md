# Back Tracking

First of all, the difference between DFS and Back tracking is subtle in implementation.
My back tracking template use stack to store states.

Pruning and optimization are useful techniques to reduce the time complexity:

1. sort the original sequence
2. exclude redundant information
3. pruning based on **target state**
4. optimization based on **current optimal answer**

## Type 1: Array

``` py
ans = []
stk = []
def dfs(i):
    if CONDITION: return ans.append(stk.copy())
    for j in range(`arg`):
        stk.append(A[j])
        dfs(j)
        stk.pop()

dfs(0)
return ans
```

## Type 2: Graph

``` py
D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
def dfs(x, y):
    if CONDITION: return STH
    tmp = A[x][y]
    A[x][y] = '#'
    for dx, dy in D:
        if 0<=x+dx<len(A) and 0<=y+dy<len(A[0]) and CONDITION: 
            dfs(x+dx, y+dy, i+1)
    A[x][y] = tmp
    return STH
            
for i in range(len(A)):
    for j in range(len(A[0])):
        CONDITION
return STH
```
