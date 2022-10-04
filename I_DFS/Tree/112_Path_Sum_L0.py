""" https://leetcode.com/problems/path-sum/
"""
from header import *

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], t: int) -> bool:
        def dfs(node, sm):
            if not node: return False
            if not node.left and not node.right:
                return sm+node.val==t
            
            l = dfs(node.left, sm+node.val)
            r = dfs(node.right, sm+node.val)
            return l or r
        
        return dfs(root, 0)