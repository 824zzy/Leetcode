# Template for back-tracking

``` py
self.ans = []
def dfs(`args`):
    if `condition`:
        self.ans.append(`ans`)
        return
    for i in range(`arg`):
        if `condition`:
            dfs(`args`)
dfs([], target)
return self.ans
```
