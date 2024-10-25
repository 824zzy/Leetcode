""" https://leetcode.com/problems/flip-equivalent-binary-trees/
post-order traversal, there are two conditions for any node:
1 - don't flip
2 - flip
"""

from header import *


class Solution:
    def flipEquiv(self, X: Optional[TreeNode], Y: Optional[TreeNode]) -> bool:
        def dfs(x, y):
            if not x and not y:
                return True
            if not x or not y:
                return False
            if x.val == y.val:
                # don't flip
                l, r = dfs(x.left, y.left), dfs(x.right, y.right)
                # flip
                fl, fr = dfs(x.left, y.right), dfs(x.right, y.left)
                return (l and r) or (fl and fr)
            else:
                return False

        return dfs(X, Y)
