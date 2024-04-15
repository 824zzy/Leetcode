""" https://leetcode.com/problems/find-all-the-lonely-nodes/
"""
from header import *


class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []

        def dfs(node):
            if not node:
                return
            if node.left and not node.right:
                self.ans.append(node.left.val)
            if node.right and not node.left:
                self.ans.append(node.right.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return self.ans
