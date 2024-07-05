""" https://leetcode.com/problems/correct-a-binary-tree/
find the abnormal node and return the correct tree
"""
from header import *


class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        seen = defaultdict(set)

        def dfs(node, d):
            if not node:
                return None
            if node.right and node.right.val in seen[d]:
                return None
            seen[d].add(node.val)
            node.right = dfs(node.right, d + 1)
            node.left = dfs(node.left, d + 1)
            return node

        return dfs(root, 0)
