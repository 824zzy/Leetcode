class Solution:
    def tree2str(self, t: TreeNode) -> str:
        def dfs(node):
            if not node:
                return ""
            if not node.left and not node.right:
                return str(node.val)
            if not node.right:
                return str(node.val)+'('+dfs(node.left)+')'
            l = dfs(node.left)
            r = dfs(node.right)
            s = str(node.val)+'('+l+')('+r+')'
            return s
        ans = dfs(t)
        return ans