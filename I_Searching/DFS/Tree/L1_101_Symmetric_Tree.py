""" https://leetcode.com/problems/symmetric-tree/
"""
from header import *


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(l, r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            if l.val != r.val:
                return False
            return dfs(l.left, r.right) and dfs(l.right, r.left)
        return dfs(root, root)
