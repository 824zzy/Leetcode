""" https://leetcode.com/problems/range-sum-of-bst/
dfs tree while check if value in range
"""
from header import *

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node: return 0
            if low<=node.val<=high:
                l = dfs(node.left)
                r = dfs(node.right)
                return node.val+l+r
            elif node.val<low:
                return dfs(node.right)
            elif node.val>high:
                return dfs(node.left)

        return dfs(root)