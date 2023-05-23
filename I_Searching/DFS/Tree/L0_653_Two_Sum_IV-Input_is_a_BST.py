""" https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
two-sum like problem, use set to find if k-node.val is existed.
"""
from header import *

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        
        def dfs(node):
            if not node: return False
            if k-node.val in seen: return True
            seen.add(node.val)
            l = dfs(node.left)
            r = dfs(node.right)
            return l or r
        
        return dfs(root)