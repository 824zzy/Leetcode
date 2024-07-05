""" https://leetcode.com/problems/leaf-similar-trees/description/
in-order dfs traversal
"""
from header import *


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]
            l = dfs(node.left)
            r = dfs(node.right)
            return l + r

        return dfs(root1) == dfs(root2)
