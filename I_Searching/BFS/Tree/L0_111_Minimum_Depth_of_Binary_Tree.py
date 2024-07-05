""" https://leetcode.com/problems/minimum-depth-of-binary-tree/
"""
from header import *


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return inf
            if not node.left and not node.right:
                return 1
            l = dfs(node.left)
            r = dfs(node.right)
            return min(l, r) + 1

        ans = dfs(root)
        return ans if ans != inf else 0


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        d = 1
        q = [(root, d)]
        while q:
            cur, dep = q.pop(0)
            if not cur.left and not cur.right:
                return dep
            if cur.left:
                q.append((cur.left, dep + 1))
            if cur.right:
                q.append((cur.right, dep + 1))
