""" https://leetcode.com/problems/find-bottom-left-tree-value/
"""
from header import *

# bfs solution


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        Q = [root]
        while Q:
            nxtQ = []
            for i, node in enumerate(Q):
                if i == 0:
                    ans = node.val
                if node.left:
                    nxtQ.append(node.left)
                if node.right:
                    nxtQ.append(node.right)
            Q = nxtQ
        return ans


# dfs solution
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.ans = {}

        def dfs(node, d):
            if not node:
                return
            dfs(node.left, d + 1)
            self.ans.setdefault(d, node.val)
            dfs(node.right, d + 1)

        dfs(root, 0)
        return self.ans[max(self.ans)]
