""" https://leetcode.com/problems/same-tree/
traverse two trees at the same time
"""
from header import *


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            else:
                if p.val != q.val:
                    return False
                l = dfs(p.left, q.left)
                r = dfs(p.right, q.right)
                return l and r

        return dfs(p, q)
