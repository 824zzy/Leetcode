""" https://leetcode.com/problems/binary-tree-level-order-traversal/
recursion solution: use defaultdict to record level nodes
"""
from collections import defaultdict


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = defaultdict(list)

        def dfs(node, d):
            if not node:
                return
            ans[d].append(node.val)
            dfs(node.left, d + 1)
            dfs(node.right, d + 1)

        dfs(root, 0)
        return ans.values()
