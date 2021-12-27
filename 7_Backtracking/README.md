# Template for back-tracking

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
