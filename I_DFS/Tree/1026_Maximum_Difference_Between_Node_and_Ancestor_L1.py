""" https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
For each subtree, find the minimum value and maximum value of its descendants.
"""
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
    
        def dfs(node):
            if not node: return inf, -inf
            l_mi, l_ma = dfs(node.left)
            r_mi, r_ma = dfs(node.right)
            mi = min(node.val, l_mi, r_mi)
            ma = max(node.val, l_ma, r_ma)
            self.ans = max(self.ans, abs(node.val-mi), abs(node.val-ma))
            return mi, ma
        
        dfs(root)
        return self.ans
    
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, ma, mi):
            if not node: return ma-mi
            ma, mi = max(ma, node.val), min(mi, node.val)
            l = dfs(node.left, ma, mi)
            r = dfs(node.right, ma, mi)
            return max(l, r)
        
        return dfs(root, -inf, inf)