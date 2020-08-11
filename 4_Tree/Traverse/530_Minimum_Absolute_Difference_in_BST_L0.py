class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.ans = float('inf')
        self.prev = float('-inf')
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            self.ans = min(self.ans, node.val-self.prev)
            self.prev = node.val
            dfs(node.right)
        
        dfs(root)
        return self.ans