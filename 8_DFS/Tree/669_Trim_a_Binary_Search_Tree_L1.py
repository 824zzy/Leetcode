""" https://leetcode.com/problems/trim-a-binary-search-tree/
"""
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        def dfs(node):
            if not node: return node
            if node.val<low: return dfs(node.right)
            if node.val>high: return dfs(node.left)
            
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            return node
        
        return dfs(root)