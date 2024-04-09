""" https://leetcode.com/problems/maximum-width-of-binary-tree/
if we label the node of each level nodes by column from 0 to n, then we have:
node.left.column = node.column*2
node.right.column = node.column*2+1
"""
from header import *


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = defaultdict(list)

        def dfs(node, l, col):
            if not node:
                return
            self.ans[l].append(col)
            dfs(node.left, l + 1, col * 2)
            dfs(node.right, l + 1, col * 2 + 1)

        dfs(root, 0, 0)
        return max(v[-1] - v[0] + 1 for _, v in self.ans.items())
