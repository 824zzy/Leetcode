""" https://leetcode.com/problems/next-greater-element-ii/
next greater template using monotonic increasing stack
"""
from header import *

class Solution:
    def nextGreaterElements(self, A: List[int]) -> List[int]:
        n = len(A)
        ans = [-1]*n
        stk = []
        for i in range(2*n):
            while stk and A[stk[-1]]<A[i%n]:
                ans[stk.pop()] = A[i%n]
            stk.append(i%n)
        return ans