class Solution:
    def rob(self, root: TreeNode) -> int:
        self.ans = {}
        
        def dfs(node):
            if not node: return 0
            if node in self.ans: return self.ans[node]
            val = 0
            if node.left:
                val += dfs(node.left.left) + dfs(node.left.right)
            if node.right:
                val += dfs(node.right.left) + dfs(node.right.right)
            val = max(val+node.val, dfs(node.left)+dfs(node.right))
            self.ans[node] = val
            return val

        return dfs(root)