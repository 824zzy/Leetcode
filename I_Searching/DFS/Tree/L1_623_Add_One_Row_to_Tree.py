""" https://leetcode.com/problems/add-one-row-to-tree/
"""
from header import *


class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            new = TreeNode(v)
            new.left = root
            return new

        def dfs(node, dep):
            if not node:
                return
            if dep == d - 1:
                newL = TreeNode(v)
                newL.left = node.left
                node.left = newL
                newR = TreeNode(v)
                newR.right = node.right
                node.right = newR
                return
            dfs(node.left, dep + 1)
            dfs(node.right, dep + 1)
        dfs(root, 1)
        return root


class Solution:
    def addOneRow(
            self,
            root: Optional[TreeNode],
            v: int,
            d: int) -> Optional[TreeNode]:
        def dfs(node, _d, c):
            if not node:
                if _d == d:
                    return TreeNode(v)
                else:
                    return
            if _d == d:
                newNode = TreeNode(v)
                if c == 'l':
                    newNode.left = node
                else:
                    newNode.right = node
                return newNode
            else:
                node.left = dfs(node.left, _d + 1, 'l')
                node.right = dfs(node.right, _d + 1, 'r')
                return node

        return dfs(root, 1, 'l')
