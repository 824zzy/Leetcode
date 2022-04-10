""" https://leetcode.com/problems/balanced-binary-tree/submissions/
For each node, check the absolute difference of subtree height.
"""
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        
        def dfs(node):
            if not node: return 1
            l = dfs(node.left)
            r = dfs(node.right)
            if abs(l-r)>1: self.ans = False
            return 1+max(l, r)
        
        dfs(root)
        return self.ans