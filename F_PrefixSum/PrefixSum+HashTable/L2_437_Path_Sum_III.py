""" https://leetcode.com/problems/path-sum-iii/
prefix sum + dfs
use prefix sum to find target subarray through back tracking
"""
from header import *

# online solution


class Solution:
    def pathSum(self, root: Optional[TreeNode], t: int) -> int:
        seen = Counter([0])
        self.ans = 0

        def dfs(node, prefix):
            if not node:
                return 0
            prefix += node.val
            self.ans += seen[prefix - t]
            seen[prefix] += 1
            dfs(node.left, prefix)
            dfs(node.right, prefix)
            seen[prefix] -= 1

        dfs(root, 0)
        return self.ans
