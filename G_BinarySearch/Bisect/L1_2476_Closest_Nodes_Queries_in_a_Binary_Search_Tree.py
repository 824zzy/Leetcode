""" https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/description/
1. convert BST to array
2. use binary search to find the closest node
"""
from header import *


class Solution:
    def closestNodes(self,
                     root: Optional[TreeNode],
                     queries: List[int]) -> List[List[int]]:
        A = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            A.append(node.val)
            dfs(node.right)
        dfs(root)

        ans = []
        for q in queries:
            x = bisect_left(A, q)
            if x == 0:
                if A[x] == q:
                    ans.append([A[0], A[0]])
                else:
                    ans.append([-1, A[0]])
            elif x == len(A):
                ans.append([A[-1], -1])
            elif A[x] == q:
                ans.append([A[x], A[x]])
            else:
                ans.append([A[x - 1], A[x]])
        return ans
