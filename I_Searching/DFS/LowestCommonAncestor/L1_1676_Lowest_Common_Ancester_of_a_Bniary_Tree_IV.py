""" https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/
the LCA template can be generalized to n nodes
"""
from header import *


class Solution:
    def lowestCommonAncestor(
            self,
            root: 'TreeNode',
            nodes: 'List[TreeNode]') -> 'TreeNode':
        vals = set(n.val for n in nodes)

        def dfs(node):
            if not node:
                return
            if node.val in vals:
                return node
            l = dfs(node.left)
            r = dfs(node.right)
            if l and r:
                return node
            return l or r
        return dfs(root)
