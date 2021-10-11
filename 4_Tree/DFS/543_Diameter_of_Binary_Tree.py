""" L0: https://leetcode.com/problems/diameter-of-binary-tree/
return max(l, r) + 1
"""
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node):
            if not node: return 0
            l = dfs(node.left)
            r = dfs(node.right)
            self.ans = max(self.ans, l+r)
            return max(l, r)+1
        
        dfs(root)
        return self.ans