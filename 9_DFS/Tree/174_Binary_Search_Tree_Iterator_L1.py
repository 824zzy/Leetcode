# Iterative: O(h), O(1)
class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stk = []
        while root:
            self.stk.append(root)
            root = root.left
    
    def next(self) -> int:
        top = self.stk.pop()
        cur = top.right
        while cur:
            self.stk.append(cur)
            cur = cur.left
        return top.val
        
    def hasNext(self) -> bool:
        return len(self.stk)>0

# Recursive: O(1), O(N)    
class BSTIterator:
    def __init__(self, root: TreeNode):
        self.node = []
        self.idx = 0
        self.dfs(root)
        self.l = len(self.node)
    
    def dfs(self, node):
        if not node:
            return False
        self.dfs(node.left)
        self.node.append(node.val)
        self.dfs(node.right)
    
    def next(self) -> int:
        self.idx += 1
        return self.node[self.idx-1]
        
    def hasNext(self) -> bool:
        return self.idx<self.l