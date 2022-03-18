# Depth First Search(DFS)

First of all, the difference between DFS and Back tracking is subtle in implementation.
My back tracking template use stack to store states.

Pruning and optimization are useful techniques to reduce the time complexity:

1. sort the original sequence
2. exclude redundant information
3. pruning based on **target state**
4. optimization based on **current optimal answer**

``` py
ans = []
stk = []
def dfs(i):
    if `logic`: return ans.append(stk.copy())
    for j in range(`arg`):
        stk.append(A[j])
        dfs(j)
        stk.pop()

dfs(0)
return ans
```
