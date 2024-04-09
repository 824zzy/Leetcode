""" https://leetcode.com/problems/binary-tree-preorder-traversal/
"""
from header import *


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stk = []
        node = root

        while stk or node:
            if node:
                ans.append(node.val)
                stk.append(node)
                node = node.left
            else:
                node = stk.pop()
                node = node.right
        return ans
