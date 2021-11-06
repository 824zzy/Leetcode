""" L1: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node: return None
            if node==p or node==q: return node
            l, r = dfs(node.left), dfs(node.right)
            if l and r: return node
            return l or r
        
        ans = dfs(root)
        return ans