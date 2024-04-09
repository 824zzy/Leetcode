""" https://leetcode.com/problems/binary-tree-inorder-traversal/
tree dfs template
"""
from header import *


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.ans = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.ans.append(node.val)
            dfs(node.right)

        dfs(root)
