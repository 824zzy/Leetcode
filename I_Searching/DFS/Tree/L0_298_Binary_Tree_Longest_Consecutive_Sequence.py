""" https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/
carefully read the problem and use dfs
"""


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node, d, p):
            self.ans = max(self.ans, d)
            if not node:
                return
            if p is not None and node.val == p + 1:
                dfs(node.left, d + 1, node.val)
                dfs(node.right, d + 1, node.val)
            else:
                dfs(node.left, 1, node.val)
                dfs(node.right, 1, node.val)

        dfs(root, 1, None)
        return self.ans
