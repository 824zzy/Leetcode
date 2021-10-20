""" L1: https://leetcode.com/problems/invert-binary-tree/
famous question
"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node: return None
            l = dfs(node.left)
            r = dfs(node.right)
            node.left, node.right = r, l
            return node
        
        return dfs(root)