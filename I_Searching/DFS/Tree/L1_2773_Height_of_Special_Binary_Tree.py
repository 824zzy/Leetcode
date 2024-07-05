""" https://leetcode.com/problems/height-of-special-binary-tree/
1. identify leaves which can be visited twice
2. dfs to find max depth
"""
from header import *


class Solution:
    def heightOfTree(self, root: Optional[TreeNode]) -> int:
        # 1
        Q = [root]
        seen = Counter([root.val])
        ans = 0
        while Q:
            nxtQ = []
            for node in Q:
                if node.left and seen[node.left.val] < 2:
                    seen[node.left.val] += 1
                    nxtQ.append(node.left)
                if node.right and seen[node.right.val] < 2:
                    seen[node.right.val] += 1
                    nxtQ.append(node.right)
            Q = nxtQ
        leaves = set([x for x in seen if seen[x] == 2])
        # 2

        def dfs(node):
            if not node:
                return 0
            if node.val in leaves:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            return max(l, r) + 1

        return dfs(root)


""" Inspired by official hint
1. identify leaves by:
    1. For some node v, if v.left == null or v.right == null, then v is not a leaf.
    2. If the previous condition does not hold, and v.left.right == v, then v is a leaf node.
2. dfs to find max depth
"""


class Solution:
    def heightOfTree(self, root: Optional[TreeNode]) -> int:
        # 1
        self.leaves = set()

        def findLeaves(node):
            if not node:
                return
            if node.left and node.left.right == node:
                self.leaves.add(node.val)
            else:
                findLeaves(node.left)
                findLeaves(node.right)

        findLeaves(root)
        # 2

        def dfs(node):
            if not node:
                return 0
            if node.val in self.leaves:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            return max(l, r) + 1

        return dfs(root)
