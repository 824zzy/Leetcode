# Note

## BottomUp / DFS

"""py
def dfs(node, args):
    if not node:
        return 0/None
    node.left = dfs(node.left)
    node.right = dfs(node.right)
    # do sth
    return node
"""

## BFS

``` py
queue = [root]
while queue:
    curr = queue.pop(0)
    `logic`
    queue.append(curr.left)
    queue.append(curr.right)
```
