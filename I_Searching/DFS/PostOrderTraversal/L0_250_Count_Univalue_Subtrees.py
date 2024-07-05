""" https://leetcode.com/problems/count-univalue-subtrees/
use set to store the value of subtree
"""
from header import *


class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        @cache
        def dfs(node):
            if not node:
                return set()
            l = dfs(node.left)
            r = dfs(node.right)
            if len(l | r | set([node.val])) == 1:
                self.ans += 1
            return l | r | set([node.val])

        dfs(root)
        return self.ans


class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        @cache
        def dfs(node):
            if not node:
                return 0, None
            if not node.left and not node.right:
                return 0, node.val
            lc, lv = dfs(node.left)
            rc, rv = dfs(node.right)
            if lv == rv == node.val:
                return lc + rc + 1, node.val
            return lc + rc, None

        return dfs(root)[0]
