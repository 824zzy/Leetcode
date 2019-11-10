# Facebook
class Solution:
    ans = 0
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return
            if not node.left and not node.right:
                return node.val
            left = dfs(node.left)
            right = dfs(node.right)
            if left:
                self.ans += left
        dfs(root)
        return self.ans