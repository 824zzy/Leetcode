""" L1: https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
"""
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, ma, mi):
            if not node: return ma-mi
            ma, mi = max(ma, node.val), min(mi, node.val)
            l = dfs(node.left, ma, mi)
            r = dfs(node.right, ma, mi)
            return max(l, r)
        
        return dfs(root, -inf, inf)