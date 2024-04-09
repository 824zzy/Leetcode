""" https://leetcode.com/problems/find-mode-in-binary-search-tree/submissions/
find the most frequent node by counter
"""
from header import *


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        M = Counter()

        def dfs(node):
            if not node:
                return
            M[node.val] += 1
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        t = max(M.values())
        return [k for k, v in M.items() if v == t]
