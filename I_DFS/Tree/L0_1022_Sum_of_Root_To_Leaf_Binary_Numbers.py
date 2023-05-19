""" https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
dfs + bit manipulation
"""
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, val):
            if not node: return 0
            if not node.left and not node.right: return 2*val+node.val
            l = dfs(node.left, 2*val+node.val)
            r = dfs(node.right, 2*val+node.val)
            return l+r
        
        return dfs(root, 0)