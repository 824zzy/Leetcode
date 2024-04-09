""" https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/
combinations + dfs
"""
from header import *


class Solution:
    def numOfWays(self, A: List[int]) -> int:
        def dfs(A):
            if len(A) <= 2:
                return 1
            # left sub-tree
            l = [x for x in A if x < A[0]]
            # right sub-tree
            r = [x for x in A if x > A[0]]
            ll, rr = dfs(l), dfs(r)
            ans = comb(len(l) + len(r), len(r))
            return ans * ll * rr

        return (dfs(A) - 1) % (10**9 + 7)
