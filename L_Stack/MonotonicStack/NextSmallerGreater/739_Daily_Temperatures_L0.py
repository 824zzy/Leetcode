""" https://leetcode.com/problems/daily-temperatures/submissions/
use monotonic decreasing stack to keep track of first temperature larger than stack top element.
"""
from header import *

class Solution:
    def dailyTemperatures(self, A: List[int]) -> List[int]:
        R = [0]*len(A)
        stk = []
        for i in range(len(A)):
            while stk and A[stk[-1]]<A[i]:
                pre = stk.pop()
                R[pre] = i-pre
            stk.append(i)
        return R