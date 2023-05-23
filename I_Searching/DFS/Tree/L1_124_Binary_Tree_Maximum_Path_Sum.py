""" https://leetcode.com/problems/binary-tree-maximum-path-sum/
at each node find the maximum path sum
note that we need to return 0 if path sum of left subtree and right subtree are negative
"""
from header import *

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -inf
        
        def dfs(node):
            if not node: return 0
            l = dfs(node.left)
            r = dfs(node.right)
            self.ans = max(self.ans, l+node.val+r)
            return max(node.val+l, node.val+r, 0)
        
        dfs(root)
        return self.ans


# another implementation
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -inf

        def dfs(node):
            if not node: return 0
            l = dfs(node.left)
            r = dfs(node.right)
            self.ans = max(self.ans, node.val+l+r, node.val+l, node.val+r, node.val)
            return max(node.val+l, node.val+r, node.val)
        dfs(root)

        return self.ans