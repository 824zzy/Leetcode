""" https://leetcode.com/problems/distribute-coins-in-binary-tree/
use dfs to find the number of coins given to the parent.
"""


class Solution(object):
    def distributeCoins(self, root):
        self.ans = 0

        def dfs(node):
            if not node:
                return 0
            L, R = dfs(node.left), dfs(node.right)
            self.ans += abs(L) + abs(R)
            return node.val + L + R - 1

        dfs(root)
        return self.ans
