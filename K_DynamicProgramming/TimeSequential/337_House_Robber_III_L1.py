""" https://leetcode.com/problems/house-robber-iii/
tree + top down dp
use canRob to control the dp
"""
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def dfs(node):
            if not node: return 0
            ans = node.val
            if node.left: ans += dfs(node.left.left) + dfs(node.left.right)
            if node.right: ans += dfs(node.right.left) + dfs(node.right.right)
            return max(ans, dfs(node.left)+dfs(node.right))
        
        return dfs(root)
    
    
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def dfs(node, canRob):
            if not node: return 0
            if canRob: return max(node.val+dfs(node.left, False)+dfs(node.right, False), 
                                  dfs(node.left, True)+dfs(node.right, True))
            else: return dfs(node.left, True)+dfs(node.right, True)
        
        return max(dfs(root, True), dfs(root, False))