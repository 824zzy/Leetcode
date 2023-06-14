""" https://leetcode.com/problems/minimum-distance-between-bst-nodes/
"""
from header import *

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.ans = inf
        self.pre = -inf
        
        def dfs(node):
            if not node: 
                return None
            
            dfs(node.left)
            self.ans = min(self.ans, node.val-self.pre)
            self.pre = node.val
            dfs(node.right)
            return node.val
            
        dfs(root)
        return self.ans