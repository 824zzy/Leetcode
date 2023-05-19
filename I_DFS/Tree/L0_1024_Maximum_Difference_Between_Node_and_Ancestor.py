class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(node):
            if not node:
                return []
            left = dfs(node.left)
            right = dfs(node.right)
            if left+right:
                self.ans = max(self.ans, max([abs(node.val-v) for v in left+right]))
            return left+right+[node.val]
        dfs(root)
        return self.ans