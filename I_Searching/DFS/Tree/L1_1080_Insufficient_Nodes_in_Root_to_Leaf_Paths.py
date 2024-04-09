""" https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/
"""
from header import *


class Solution:
    def sufficientSubset(
            self,
            root: Optional[TreeNode],
            limit: int) -> Optional[TreeNode]:
        def dfs(node, sm):
            sm += node.val
            if not node:
                return None, False
            if not node.left and not node.right:
                if sm < limit:
                    return None, False
                else:
                    return node, True

            node.left, canL = dfs(node.left, sm)
            node.right, canR = dfs(node.right, sm)
            if not canL and not canR:
                return None, False
            else:
                return node, True

        return dfs(root, 0)[0]
