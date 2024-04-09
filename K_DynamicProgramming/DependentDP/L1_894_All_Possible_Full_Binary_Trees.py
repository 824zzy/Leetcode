""" https://leetcode.com/problems/all-possible-full-binary-trees/
Create full binary trees recursively.

Time complexity: O(2^N)
"""
from header import *


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        @cache
        def dp(n):
            if n == 1:
                return [TreeNode()]
            ans = []
            for nn in range(1, n, 2):
                for l in dp(nn):
                    for r in dp(n - 1 - nn):
                        ans.append(TreeNode(left=l, right=r))
            return ans

        return dp(n)
