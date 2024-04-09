""" https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/
tree-based backtracking along with the frequency of each number
"""
from header import *


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        seen = [0] * 10

        def dfs(node):
            if not node:
                return
            seen[node.val] += 1
            if not node.left and not node.right:
                cnt = 0
                for x in seen:
                    if x & 1:
                        cnt += 1
                seen[node.val] -= 1
                if cnt <= 1:
                    self.ans += 1
                return

            dfs(node.left)
            dfs(node.right)
            seen[node.val] -= 1

        dfs(root)
        return self.ans
