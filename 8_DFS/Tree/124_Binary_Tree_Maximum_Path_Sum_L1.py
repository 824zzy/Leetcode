""" L1: https://leetcode.com/problems/binary-tree-maximum-path-sum/
at each node find the maximum path sum
"""
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -inf
        
        def dfs(node):
            if not node: return -inf
            l = dfs(node.left)
            r = dfs(node.right)
            self.ans = max(self.ans, node.val, node.val+l, node.val+r, node.val+l+r)
            return max([node.val, node.val+l, node.val+r])
        
        ans = dfs(root)
        return self.ans