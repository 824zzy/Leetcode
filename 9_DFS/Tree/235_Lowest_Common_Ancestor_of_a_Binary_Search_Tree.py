""" L1: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
treverse BST tree
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node: return None
            if p.val<=node.val<=q.val or q.val<=node.val<=p.val: return node
            l, r = dfs(node.left), dfs(node.right)
            return l or r
        
        return dfs(root)