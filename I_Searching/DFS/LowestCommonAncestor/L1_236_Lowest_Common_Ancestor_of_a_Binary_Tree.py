""" https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
classical problem
"""
from header import *


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def dfs(node):
            if not node:
                return None
            if node == p or node == q:
                return node
            l = dfs(node.left)
            r = dfs(node.right)
            if l and r:
                return node
            return l or r

        return dfs(root)
