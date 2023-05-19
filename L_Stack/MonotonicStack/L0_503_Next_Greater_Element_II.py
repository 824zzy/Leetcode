""" https://leetcode.com/problems/next-greater-element-ii/
next greater template using monotonic increasing stack
"""
from header import *

class Solution:
    def nextGreaterElements(self, A: List[int]) -> List[int]:
        n = len(A)
        A *= 2
        ans = [-1]*len(A)
        stk = []
        for i in range(len(A)):
            while stk and A[stk[-1]]<A[i]:
                ans[stk.pop()] = A[i]
            stk.append(i)
        return ans[:n]