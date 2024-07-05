""" https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/
Slightly modify the LCA template
"""
from header import *


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        self.hasP, self.hasQ = False, False

        def dfs(node, p, q):
            if not node:
                return None
            l = dfs(node.left, p, q)
            r = dfs(node.right, p, q)
            if node == p:
                self.hasP = True
                return node
            elif node == q:
                self.hasQ = True
                return node
            elif l and r:
                return node
            else:
                return l or r

        ans = dfs(root, p, q)
        return ans if self.hasP and self.hasQ else None
