class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.sum = 0

        def dfs(node):
            if not node:
                return 0
            dfs(node.right)
            self.sum += node.val
            node.val = self.sum
            dfs(node.left)

        dfs(root)
        return root
