""" https://leetcode.com/problems/closest-binary-search-tree-value/
dfs
"""
from header import *


class Solution:
    def closestValue(self, root: Optional[TreeNode], t: float) -> int:
        self.ans = inf

        def dfs(node):
            if not node:
                return
            self.ans = min(self.ans, node.val, key=lambda x: (abs(x - t), x))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.ans
