""" https://leetcode.com/problems/clone-binary-tree-with-random-pointer/
"""
from header import *

class Solution:
    def copyRandomBinaryTree(self, root):
        mp = {}
        
        def fn(node):
            """Return cloned binary tree."""
            if not node: return 
            if node not in mp: 
                mp[node] = NodeCopy(node.val)
                mp[node].left = fn(node.left)
                mp[node].right = fn(node.right)
                mp[node].random = fn(node.random)
            return mp[node]
        
        return fn(root)