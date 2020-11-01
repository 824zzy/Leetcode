class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        v = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            v.append(node.val)
            dfs(node.right)
        dfs(root)
        v = sorted(v)
        self.curr = 0
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            node.val = v[self.curr]
            self.curr += 1
            dfs(node.right)
        dfs(root)
        return root
