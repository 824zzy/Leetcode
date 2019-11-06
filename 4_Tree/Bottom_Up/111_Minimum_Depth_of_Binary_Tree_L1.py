class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        def dfs(node, depth):
            if not node:
                return float('inf')
            if not node.left and not node.right:
                return depth
            left = dfs(node.left, depth+1)
            right = dfs(node.right, depth+1)
            return min(left, right)
        return dfs(root, 1)