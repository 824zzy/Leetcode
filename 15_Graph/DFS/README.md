# Graph DFS template

## Type 1

``` py
# TODO: test new template from: https://leetcode.com/problems/path-with-minimum-effort/
def dfs(x, y):
    for dx, dy in neibs:
        if 0<=dx+x<nr and 0<=dy+y<nc and CONDITION:
            if CONDITION:
                dfs(dx+x, dy+y)
M, N = len(grid), len(grid[0])
neibs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
ans = 0
for i in range(M):
    for j in range(N):
        if CONDITION:
            ans = LOGIC
return ans

```

## Type2

Note: visit array can be replaced by a set

``` py
from collections import defaultdict
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        n = len(M)
        g = defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                if M[i][j]==1:
                    g[i].append(j)
                    g[j].append(i)
        visit = [0] * n
        def dfs(node):
            for n in g[node]:
                if not visit[n]:
                    visit[n] = 1
                    dfs(n)
        `init_variable`
        for i in range(n):
            if not visit[i]:
                visit[i] = 1
                dfs(i)
        return ans
```
