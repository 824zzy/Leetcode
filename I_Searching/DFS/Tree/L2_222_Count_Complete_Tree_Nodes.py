""" https://leetcode.com/problems/count-complete-tree-nodes/
Idea from ye: https://leetcode.com/problems/count-complete-tree-nodes/discuss/702258/Python3-two-O(logN-*-logN)-approaches
1. compute its height h;
2. compute the height of its right child
    2.1) if it is h-1, then we know the left sub-tree is perfectly balanced whose nodes can be computed using its height;
    2.2) it it is h-2 then we know the right sub-tree is perfectly balanced;
"""
from header import *


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def height(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h

        def dfs(node):
            if not node:
                return 0
            h = height(node)
            if height(node.right) == h - 1:
                return 2**(h - 1) + dfs(node.right)
            else:
                return 2**(h - 2) + dfs(node.left)

        return dfs(root)
