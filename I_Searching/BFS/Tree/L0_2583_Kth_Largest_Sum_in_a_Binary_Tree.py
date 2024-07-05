""" https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/
level order traversal by bfs
"""
from header import *


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        T = []
        Q = [root]
        while Q:
            nxtQ = []
            sm = 0
            for node in Q:
                sm += node.val
                if node.left:
                    nxtQ.append(node.left)
                if node.right:
                    nxtQ.append(node.right)
            T.append(sm)
            Q = nxtQ

        A = sorted(T, reverse=True)
        if k - 1 < len(A):
            return A[k - 1]
        else:
            return -1


# dfs also works
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        T = defaultdict(list)

        def dfs(node, d):
            if not node:
                return
            T[d].append(node.val)
            dfs(node.left, d + 1)
            dfs(node.right, d + 1)

        dfs(root, 0)

        A = sorted([sum(x) for x in T.values()], reverse=True)
        if k - 1 < len(A):
            return A[k - 1]
        else:
            return -1
