# Graph Template

## Breadth First Search(BFS)

In Q, it maybe also stores steps and other information.
When we have to build a graph by ourself, don't forget try to reduce time complexity by some tricks.

```py
def graghBFS(self, A: List[List[int]]) -> int:
    Q = [STATE_STATE]
    seen = set()
    while Q:
        i = Q.pop(0)
        if i not in seen:
            seen.add(i)
            for NEXT_STATES:
                if CONDITION:
                    Q.append(NEXT_STATE)
```
