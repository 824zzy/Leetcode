# Graph Template

## Breadth First Search(BFS)

```py
class Solution:
    def slidingPuzzle(self, A: List[List[int]]) -> int:
        state = "from A"
        seen = set()
        queue = [state]
        while queue:
            for _ in range(len(queue)):
                state = queue.pop(0)
                if/for `logic`: `logic`
                queue.append(state)
        return ans
```

## Depth First Search(DFS)

### Type1

``` py
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        nr = len(grid)
        nc = len(grid[0])
        def dfs(grid, r, c):
            if `condition`:
                return
            logic over here # grid[r][c] = '0'
            dfs(grid, r-1, c)
            dfs(grid, r+1, c)
            dfs(grid, r, c-1)
            dfs(grid, r, c+1)
        `init_varable`
        for r in range(nr):
            for c in range(nc):
                if `condition`:
                    `do sth`
                    dfs(grid, r, c)
        return `ans`
```

``` py
# TODO: test new template from: https://leetcode.com/problems/path-with-minimum-effort/
def dfs(LIMIT, x, y):
    seen.add((x, y))
    for dx, dy in neibs:
        if 0<=dx+x<nr and 0<=dy+y<nc and (dx+x, dy+y) not in seen:
            if abs(A[x][y]-A[dx+x][dy+y])<=LIMIT:
                dfs(LIMIT, dx+x, dy+y)
```

### Type2

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
