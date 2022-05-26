# Iterative Tree Traversal by Stack

``` py
Pre order, In order, Post order: stack

def preOrder(self, root):
    ans = []
    stk = []
    node = root
    while stk or node:
        if node: 
            ans.append(node.val)
            stk.append(node)
            node = node.left
        else:
            node = stk.pop()
            node = node.right
    return ans
        
def inOrder(self, root):
    stk = []
    ans = []
    node = root
    while stk or node:
        if node:
            stk.append(node)
            node = node.left
        else:
            node = stk.pop()
            ans.append(node.val)
            node = node.right
    return ans
        
def postOrder(self, root):
    if not root: return []
    stk1 = [root]
    stk2 = []
    ans = []
    while stk1:
        node = stk1.pop()
        if node.left: stk1.append(node.left)
        if node.right: stk1.append(node.right)
        stk2.append(node)
    while stk2: ans.append(stk2.pop().val)
    return ans
```
