""" https://leetcode.com/problems/range-sum-of-bst/
dfs tree while check if value in range
"""
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], lo: int, hi: int) -> int:
        def dfs(node):
            if not node: return 0
            l = dfs(node.left)
            r = dfs(node.right)
            if lo<=node.val<=hi: return node.val+l+r
            else: return l+r
        
        return dfs(root)