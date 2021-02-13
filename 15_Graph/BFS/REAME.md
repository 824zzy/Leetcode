# Breadth First Search(BFS)

```py
class Solution:
    def graghBFS(self, A: List[List[int]]) -> int:
        seen = set()
        queue = ["state from A"]
        while queue:
            for _ in range(len(queue)):
                state = queue.pop(0)
                if/for `logic`: `logic`
                queue.append(state)
        return ans
```

## tips

go through 8 directions:

``` py
for x, y in ((i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), \
             (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)):
    if 0<=x<nr and 0<=y<nc and not grid[x][y] and (x, y) not in seen:
        `logic`
```
