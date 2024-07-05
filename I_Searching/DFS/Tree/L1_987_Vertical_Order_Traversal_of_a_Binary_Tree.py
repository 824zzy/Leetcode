""" https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
dfs + sorting

use dict of a dict to store the tree in vertical and depth order
"""
from header import *


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        T = defaultdict(list)

        def dfs(node, p, d):
            if not node:
                return
            T[p].append((d, node.val))
            dfs(node.left, p - 1, d + 1)
            dfs(node.right, p + 1, d + 1)

        dfs(root, 0, 0)

        ans = []
        for x in sorted(T.items()):
            ans.append(y[1] for y in sorted(x[1], key=lambda x: (x[0], x[1])))
        return ans
