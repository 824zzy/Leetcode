""" L1: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
classical problem
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(node): 
            if not node or node.val in (p.val, q.val): return node 
            l, r = lca(node.l), lca(node.r)
            return node if l and r else l or r
        
        return lca(root)
    
    
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node: return None
            if node==p or node==q: return node
            l, r = dfs(node.l), dfs(node.r)
            if l and r: return node
            return l or r
        
        ans = dfs(root)
        return ans
