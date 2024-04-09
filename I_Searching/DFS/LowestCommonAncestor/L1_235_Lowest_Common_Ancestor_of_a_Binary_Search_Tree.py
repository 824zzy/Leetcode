""" https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
dfs + categorization
"""
from header import *


class Solution:
    def lowestCommonAncestor(
            self,
            root: 'TreeNode',
            p: 'TreeNode',
            q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p

        def dfs(node):
            if not node:
                return None
            if p.val <= node.val <= q.val:
                return node
            elif node.val < p.val:
                return dfs(node.right)
            else:
                return dfs(node.left)
        return dfs(root)
