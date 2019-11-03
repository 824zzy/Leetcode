class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, prev: int) -> int:
            if not node:
                return 0
            left = dfs(node.left, node.val)
            right = dfs(node.right, node.right)
            self.ans = max(self.ans, left+right)
            
            if node.val == prev:
                return 1+max(left, right)
            return 0
    
    self.ans = 0
    if not root:
        return 0
    dfs(root, root.val)
    return self.ans