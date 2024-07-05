""" https://leetcode.com/problems/trapping-rain-water/
This problem is similar to 84.

Three pass template solution: find next greater element on the left and right by monotonic template, then let `min(left, right)-A[i]` as height and `r-l-1` as width, note that use seen to remove duplicates
One pass solution: dynamically assume stack pop as bottom, then the width is `i-stk[-1]-1` and height is `min(A[i], A[stk[-1]])-btm`
"""
from header import *

# three pass template solution


class Solution:
    def trap(self, A: List[int]) -> int:
        # next greater on the right
        R = [len(A)] * len(A)
        stk = []
        for i in range(len(A)):
            while stk and A[stk[-1]] < A[i]:
                R[stk.pop()] = i
            stk.append(i)

        # next greater on the left
        L = [-1] * len(A)
        stk = []
        for i in reversed(range(len(A))):
            while stk and A[stk[-1]] <= A[i]:
                L[stk.pop()] = i
            stk.append(i)

        ans = 0
        for i, (l, r) in enumerate(zip(L, R)):
            if l != -1 and r != len(A):
                ans += (min(A[l], A[r]) - A[i]) * (r - l - 1)
        return ans


# optimal one pass solution


class Solution:
    def trap(self, A: List[int]) -> int:
        stk = []
        ans = 0
        for i in range(len(A)):
            while stk and A[stk[-1]] < A[i]:
                btm = A[stk.pop()]
                # if left wall exists
                if stk:
                    w = i - stk[-1] - 1
                    h = min(A[i], A[stk[-1]]) - btm
                    ans += w * h
            stk.append(i)
        return ans
