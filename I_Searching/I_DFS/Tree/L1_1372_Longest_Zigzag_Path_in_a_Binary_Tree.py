""" https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/
post order traversal
"""
from header import *

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def dfs(node, d):
            if not node: return 0
            l = dfs(node.left, 'r')
            r = dfs(node.right, 'l')
            self.ans = max(self.ans, max(l, r))
            
            if d=='l': return 1+l
            else: return 1+r
            
        dfs(root, 'l')
        dfs(root, 'r')
        return self.ans


# neat solution from ye
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def dfs(node):
            if not node: return (0, 0)
            _, r = dfs(node.left)
            l, _ = dfs(node.right)
            self.ans = max(self.ans, l+1, r+1)
            return (r+1, l+1)
            
        dfs(root)
        return self.ans-1