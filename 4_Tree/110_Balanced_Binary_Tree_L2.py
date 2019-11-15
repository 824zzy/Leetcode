class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.ans = True
        def dfs(node, d):
            if not node:
                return d-1
            if not node.left and not node.right:
                return d
            l = dfs(node.left, d+1)
            r = dfs(node.right, d+1)
            if abs(l-r)>1:
                self.ans = False
            return max(l, r)
        dfs(root, 0)
        return self.ans