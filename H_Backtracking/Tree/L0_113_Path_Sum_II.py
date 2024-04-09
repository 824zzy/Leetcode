""" https://leetcode.com/problems/path-sum-ii/
dfs with path or backtracking
"""
from header import *


class Solution:
    def pathSum(self, root: Optional[TreeNode], t: int) -> List[List[int]]:
        ans = []
        stk = []

        def dfs(node, sm):
            if not node:
                return
            stk.append(node.val)
            if not node.left and not node.right:
                if sm + node.val == t:
                    ans.append(stk.copy())
            else:
                dfs(node.left, sm + node.val)
                dfs(node.right, sm + node.val)
            stk.pop()

        dfs(root, 0)
        return ans


class Solution:
    def pathSum(self, root: Optional[TreeNode], t: int) -> List[List[int]]:
        ans = []

        def dfs(node, sm, path):
            if not node:
                return
            if not node.left and not node.right:
                if sm + node.val == t:
                    ans.append(path + [node.val])
                return

            dfs(node.left, sm + node.val, path + [node.val])
            dfs(node.right, sm + node.val, path + [node.val])

        dfs(root, 0, [])
        return ans
