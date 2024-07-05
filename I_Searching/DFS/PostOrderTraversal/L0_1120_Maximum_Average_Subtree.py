""" https://leetcode.com/problems/maximum-average-subtree/
"""
from header import *


class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.ans = 0

        def dfs(node):
            if not node:
                return 0, 0
            l_cnt, l_sm = dfs(node.left)
            r_cnt, r_sm = dfs(node.right)
            self.ans = max(self.ans, (l_sm + r_sm + node.val) / (l_cnt + r_cnt + 1))
            return l_cnt + r_cnt + 1, l_sm + r_sm + node.val

        dfs(root)
        return self.ans
