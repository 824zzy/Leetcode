""" https://leetcode.com/problems/range-sum-of-bst/
dfs tree while check if value in range
"""
from header import *


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return 0
            ans = 0
            if node.val > low:
                ans += dfs(node.left)
            if node.val < high:
                ans += dfs(node.right)
            if low <= node.val <= high:
                ans += node.val
            return ans

        return dfs(root)
