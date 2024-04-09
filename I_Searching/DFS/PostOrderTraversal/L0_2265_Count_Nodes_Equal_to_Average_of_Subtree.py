""" https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/
dfs along with sum of value and node count

Time: O(n)
"""
from header import *


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node):
            if not node:
                return 0, 0
            l, l_cnt = dfs(node.left)
            r, r_cnt = dfs(node.right)
            if node.val == (node.val + l + r) // (1 + l_cnt + r_cnt):
                self.ans += 1
            return node.val + l + r, 1 + l_cnt + r_cnt

        dfs(root)
        return self.ans
