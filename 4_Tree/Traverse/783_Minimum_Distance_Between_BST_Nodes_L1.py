class Solution:
    def minDiffInBST(self, root: TreeNode) -> int: 
        self.ans = float('inf')
        self.prev = float('-inf')
        
        def dfs(node, prev):
            if not node:
                return
            
            dfs(node.left, self.prev)
            self.ans = min(self.ans, node.val-self.prev)
            self.prev = node.val
            dfs(node.right, self.prev)
            
        dfs(root, float('inf'))
        return self.ans