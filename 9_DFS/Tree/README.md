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

## Tree Traversal

``` py
# Recursive
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
    
# iteration
"""
Pre order, In order, Post order: stack
Level order: queue
"""
def preOrder(self, root):
    if root == None:
        return
    stack = []
    node = root
    while stack or node:
        while node:
            stack.append(node)
            print(node.val)
            node = node.left
        node = stack.pop()
        node = node.right
        
def inOrder(self, root):
    if root == None:
        return
    stack = []
    node = root
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        print(node.val)
        node = node.right
        
def postOrder(self, root):
    if root == None:
        return
    stack1 = []
    stack2 = []
    node = root
    stack1.append(node)
    while stack1:
        node = stack1.pop()
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
        stack2.append(node)
    while stack2:
        print(stack2.pop().val)
        
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
