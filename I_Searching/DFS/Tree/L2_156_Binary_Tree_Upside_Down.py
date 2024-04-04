""" https://leetcode.com/problems/binary-tree-upside-down/
"""
from header import *

class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if not root: return # edge case 
        
        def dfs(node):
            if not node.left: return node
            res = dfs(node.left)
            node.left.left = node.right
            node.left.right = node
            node.left = node.right = None 
            return res
        
        return dfs(root)