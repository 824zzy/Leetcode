class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.res = 0
        def dfs(node: TreeNode) -> None:
            if not node:
                return
            dfs(node.left)
            self.k -= 1
            if self.k == 0:
                self.res = node.val
            else:
                dfs(node.right)
        
        dfs(root)
        return self.res