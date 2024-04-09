""" https://leetcode.com/problems/construct-string-from-binary-tree/
dfs but need to consider the case when right child is None
"""
from header import *


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(node):
            if not node:
                return ''
            if not node.left and not node.right:
                return str(node.val)
            l = "(" + dfs(node.left) + ")"
            r = "(" + dfs(node.right) + ")"
            if r == '()':
                r = ''
            return str(node.val) + l + r
        return dfs(root)
