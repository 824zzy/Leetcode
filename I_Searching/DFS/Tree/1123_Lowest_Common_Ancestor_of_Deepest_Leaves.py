""" L1: https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/
get subtree deepest depth, same idea of 865
"""


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.ans = None
        self.deepest = 0

        def dfs(node, d):
            self.deepest = max(self.deepest, d)
            if not node:
                return d
            l = dfs(node.left, d + 1)
            r = dfs(node.right, d + 1)
            if l == r == self.deepest:
                self.ans = node
            return max(l, r)

        dfs(root, 0)
        return self.ans
