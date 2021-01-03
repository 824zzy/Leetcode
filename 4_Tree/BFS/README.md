# Tree Iterative BFS template

```py
def tree_BFS(self, root: TreeNode) -> int:
    queue = [root]
    `define ans`
    while queue:
        for i in range(len(queue)):
            cur = queue.pop(0)
            if cur.left: queue.append(cur.left)
            if cur.right: queue.append(cur.right)
    return `define ans`
```
