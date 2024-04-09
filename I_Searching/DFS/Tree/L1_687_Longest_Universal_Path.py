""" https://leetcode.com/problems/longest-univalue-path/
record previous node's value to find maximum length path
"""


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node, prev):
            if not node:
                return 0
            l = dfs(node.left, node.val)
            r = dfs(node.right, node.val)
            self.ans = max(self.ans, l + r)
            if node.val == prev:
                return 1 + max(l, r)
            else:
                return 0

        self.ans = 0
        dfs(root, inf)
        return self.ans
