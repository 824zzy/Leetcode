class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.prev = 0
        def dfs(node: TreeNode) -> Node:
            if not node:
                return
            dfs(node.right)
            node.val += self.prev
            self.prev = node.val
            dfs(node.left)
        
        dfs(root)
        return root