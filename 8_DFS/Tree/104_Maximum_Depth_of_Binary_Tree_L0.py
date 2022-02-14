""" https://leetcode.com/problems/maximum-depth-of-binary-tree/
Find maximum depth at each node through dfs
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node: return 0
            l = dfs(node.left)
            r = dfs(node.right)
            return 1+max(l, r)
            
        return dfs(root)