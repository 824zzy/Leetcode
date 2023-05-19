""" https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
check node value along with traverse BST tree
"""
from header import *

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node: return None
            if p.val<=node.val<=q.val or q.val<=node.val<=p.val: return node
            l, r = dfs(node.left), dfs(node.right)
            return l or r
        
        return dfs(root)

# solution using global variable
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p, q = min(p.val, q.val), max(p.val, q.val)
        self.ans = None
        
        def dfs(node):
            if p<=node.val<=q:
                self.ans = node
                return
            if p<q<node.val:
                dfs(node.left)
            else:
                dfs(node.right)
                
        dfs(root)
        return self.ans