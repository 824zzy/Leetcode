""" https://leetcode.com/problems/sum-root-to-leaf-numbers/
find leaves and calculate sum
"""
from header import *


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, x):
            if not node:
                return 0
            if not node.left and not node.right:
                return x * 10 + node.val
            return dfs(node.left, x * 10 + node.val) + dfs(
                node.right, x * 10 + node.val
            )

        return dfs(root, 0)
