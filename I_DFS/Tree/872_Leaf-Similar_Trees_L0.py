""" https://leetcode.com/problems/leaf-similar-trees/description/
in-order dfs traversal
"""
from header import *

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(node):
            if not node: 
                return []
            if not node.left and not node.right:
                return [node.val]
            ans = []
            ans += dfs(node.left)
            ans += dfs(node.right)
            return ans
        
        return dfs(root1)==dfs(root2)