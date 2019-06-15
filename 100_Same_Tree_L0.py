""" Easy recursive solution
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p or not q:
            return p == q
        elif p.val != q.val:
            return False 
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)