""" https://leetcode.com/problems/cousins-in-binary-tree-ii/
the sum of all cousins' values = sum of all same level nodes' values - parent's children's value
"""
from header import *


class Solution:
    def replaceValueInTree(
            self,
            root: Optional[TreeNode]) -> Optional[TreeNode]:
        T = defaultdict(int)
        P = defaultdict(int)

        def dfs(node, p, d):
            if not node:
                return
            dfs(node.left, node, d + 1)
            T[d] += node.val
            P[p] += node.val
            dfs(node.right, node, d + 1)
        dfs(root, None, 0)

        def dfs(node, p, d):
            if not node:
                return
            dfs(node.left, node, d + 1)
            node.val = T[d] - P[p]
            dfs(node.right, node, d + 1)
            return node
        return dfs(root, None, 0)
