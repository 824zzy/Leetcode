""" https://leetcode.com/problems/balance-a-binary-search-tree/
1. collect value by inorder traversal
2. build balanced BST by divide and conquer
"""
from header import *

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        vals = []
        def dfs(node):
            if not node: return
            dfs(node.left)
            vals.append(node.val)
            dfs(node.right)
        dfs(root)
        
        def fn(i, j):
            if i>j: return
            node = TreeNode(vals[(i+j)//2])
            node.left = fn(i, (i+j)//2-1)
            node.right = fn((i+j)//2+1, j)
            return node
        
        return fn(0, len(vals)-1)