# Facebook
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(node, lower, upper):
            if not node:
                return True
            if node.val>=upper or node.val<=lower:
                return False
            l = dfs(node.left, lower, node.val)
            r = dfs(node.right, node.val, upper)
            return l and r
        ans = dfs(root, float('-inf'), float('inf'))
        return ans