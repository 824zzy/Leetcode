# Note

## BottomUp / DFS

Recursive version

``` py
def dfs(node, args):
    if not node: return 0/None
    l = dfs(node.left)
    r = dfs(node.right)
    # do sth
    return # sth
```

Iterative version

``` py
stack = [root]
while stack:
    curr = stack.pop()
    `logic`
    stack.append(curr.right)
    stack.append(curr.left)
```

## Tree Traversal

**Recursive version**:

``` py
def preOrder(self, root):
    if root == None:
        return
    print(root.val)
    self.preOrder(self, root.left)
    self.preOrder(self, root.right)
    
def inOrder(self, root):
    if root == None:
        return
    self.inorder(self, root.left)
    print(root.val)
    self.inorder(self, root.right)
    
def postOrder(self, root):
    if root == None:
        return
    self.postOrder(self, root.left)
    self.postOrder(self, root.right)
    print(root.val)
    
        
# level order
def levelOrder(self, root):
    queue = [root]
    node = root
    while queue:
        node = queue.pop(0)
        print(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```

## Lowest common ancestor

**LCA template**:

``` py
def lca(node): 
    """Return lowest common ancestor of start and dest nodes."""
    if not node or node.val in (startValue , destValue): return node 
    left, right = lca(node.left), lca(node.right)
    return node if left and right else left or right
```
