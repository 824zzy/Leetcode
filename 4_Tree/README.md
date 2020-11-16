# Note

## BottomUp / DFS

Recursive version
"""py
def dfs(node, args):
    if not node:
        return 0/None
    node.left = dfs(node.left)
    node.right = dfs(node.right)
    # do sth
    return node
"""

Iterative version

``` py
stack = [root]
while stack:
    curr = stack.pop()
    `logic`
    stack.append(curr.right)
    stack.append(curr.left)
```

## BFS

Iterative version

``` py
queue = [root]
while queue:
    curr = queue.pop(0)
    `logic`
    queue.append(curr.left)
    queue.append(curr.right)
```
