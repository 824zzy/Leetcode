""" https://leetcode.com/problems/smallest-string-starting-from-leaf/
dfs simulation
"""
from header import *


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.ans = "z" * 8501

        def dfs(node, s):
            if not node:
                return
            if not node.left and not node.right:
                s += chr(97 + node.val)
                s = "".join(s[::-1])
                self.ans = min(self.ans, s)
                return

            dfs(node.left, s + chr(97 + node.val))
            dfs(node.right, s + chr(97 + node.val))

        dfs(root, "")
        return self.ans
