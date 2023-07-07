""" https://leetcode.com/problems/count-univalue-subtrees/
"""
from header import *

# use set to store the value of subtree
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        @cache
        def dfs(node):
            if not node: return set()
            l = dfs(node.left)
            r = dfs(node.right)
            if len(l|r|set([node.val]))==1:
                self.ans += 1
            return l|r|set([node.val])

        dfs(root)
        return self.ans