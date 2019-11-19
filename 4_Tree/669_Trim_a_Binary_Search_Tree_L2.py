class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        def dfs(node):
            if not node:
                return
            if L<=node.val<=R:
                node.left = dfs(node.left)
                node.right = dfs(node.right)
            elif node.val<L:
                node = dfs(node.right)
            else:
                node = dfs(node.left)
            return node
        ans = dfs(root)
        return ans