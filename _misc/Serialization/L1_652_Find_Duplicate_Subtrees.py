""" https://leetcode.com/problems/find-duplicate-subtrees/
serialization(pre-order dfs)
"""
from header import *


class Solution:
    def findDuplicateSubtrees(
        self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        seen = defaultdict(set)

        def dfs(node):
            if not node:
                return "#"
            l = dfs(node.left)
            r = dfs(node.right)
            cur = "(" + l + ")" + str(node.val) + "(" + r + ")"
            seen[cur].add(node)
            return cur

        dfs(root)

        return [v.pop() for k, v in seen.items() if len(v) > 1]
