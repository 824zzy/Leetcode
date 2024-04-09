""" https://leetcode.com/problems/extract-kth-character-from-the-rope-tree/
inorder traversal
"""
from header import *


class Solution:
    def getKthCharacter(self, root: Optional[object], k: int) -> str:
        def dfs(node, k):
            if not node:
                return 0, ''
            if not node.left and not node.right:
                if k - 1 < len(node.val):
                    return k, node.val[k - 1]
                else:
                    return len(node.val), ''

            l, ans_l = dfs(node.left, k)
            r, ans_r = dfs(node.right, k - l)
            return l + r, ans_l or ans_r

        return dfs(root, k)[1]


class Solution:
    def getKthCharacter(self, root: Optional[object], k: int) -> str:
        def dfs(node):
            if not node:
                return ''
            if not node.left and not node.right:
                return node.val

            l = dfs(node.left)
            r = dfs(node.right)
            return l + r

        return dfs(root)[k - 1]
