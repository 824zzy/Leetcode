""" https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/
mono stack or divide and conquer
"""
from header import *


class Solution:
    def verifyPreorder(self, A: List[int]) -> bool:
        # monotonic decreasing stack
        stk = []
        # keep track of minimum valid value
        mn = -inf
        for x in A:
            if x < mn:
                return False
            while stk and stk[-1] < x:
                mn = stk.pop()
            stk.append(x)
        return True


# divide and conquer
class Solution:
    def verifyPreorder(self, A: List[int]) -> bool:
        def dc(i, lo, hi):
            if i == len(A):
                return -1
            if not lo < A[i] < hi:
                return i
            l = dc(i + 1, lo, A[i])
            if l == -1:
                return l
            else:
                return dc(l, A[i], hi)

        return dc(0, -inf, inf) == -1


"""
[5,2,1,3,6]
[5,2,6,1,3]
"""
