""" https://leetcode.com/problems/house-robber-iii/
tree + top down dp
use canRob to control the dp
"""
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @lru_cache(None)
        def dfs(node, canRob):
            if not node: return 0
            if canRob: return max(node.val+dfs(node.left, False)+dfs(node.right, False), 
                                  dfs(node.left, True)+dfs(node.right, True))
            else: return dfs(node.left, True)+dfs(node.right, True)
        
        return max(dfs(root, True), dfs(root, False))