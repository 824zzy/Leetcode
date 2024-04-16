""" https://leetcode.com/problems/add-one-row-to-tree/
Tree simulation
"""
from header import *


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def dfs(node, d, is_left):
            if d == depth:
                new_node = TreeNode(val)
                if is_left:
                    new_node.left = node
                else:
                    new_node.right = node
                return new_node
            if not node:
                return
            l = dfs(node.left, d+1, True)
            r = dfs(node.right, d+1, False)
            node.left = l
            node.right = r
            return node

        return dfs(root, 1, True)
