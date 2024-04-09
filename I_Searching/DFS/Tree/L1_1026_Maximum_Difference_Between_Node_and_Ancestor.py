""" https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
For each subtree, find the minimum value and maximum value of its descendants.
"""
from header import *


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node):
            if not node:
                return inf, -inf
            if not node.left and not node.right:
                return node.val, node.val

            mn1, mx1 = dfs(node.left)
            mn2, mx2 = dfs(node.right)
            mn = min(mn1, mn2, node.val)
            mx = max(mx1, mx2, node.val)
            self.ans = max(self.ans, abs(node.val - mn), abs(node.val - mx))
            return mn, mx

        dfs(root)
        return self.ans


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, ma, mi):
            if not node:
                return ma - mi
            ma, mi = max(ma, node.val), min(mi, node.val)
            l = dfs(node.left, ma, mi)
            r = dfs(node.right, ma, mi)
            return max(l, r)

        return dfs(root, -inf, inf)
