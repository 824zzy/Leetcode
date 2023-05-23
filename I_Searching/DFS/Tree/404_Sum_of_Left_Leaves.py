""" L0: https://leetcode.com/problems/sum-of-left-leaves/
traverse tree with label that marks left tree
"""
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, l):
            if not node: return 0
            if not node.left and not node.right and l:
                return node.val
            
            return dfs(node.left, True)+dfs(node.right, False)
        
        return dfs(root, False)