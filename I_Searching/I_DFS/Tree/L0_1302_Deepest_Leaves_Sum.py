""" https://leetcode.com/problems/deepest-leaves-sum/
dfs with deepest node value and depth
"""
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node: return 0, 0
            elif not node.left and not node.right: return node.val, 1
            l, ld = dfs(node.left)
            r, rd = dfs(node.right)
            if ld==rd: return l+r, ld+1
            elif ld>rd: return l, ld+1
            else: return r, rd+1
            
        return dfs(root)[0]