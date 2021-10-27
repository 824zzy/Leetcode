""" L1: https://leetcode.com/problems/invert-binary-tree/
famous question
"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node: return None
            node.left, node.right = dfs(node.right), dfs(node.left)
            return node
        return dfs(root)