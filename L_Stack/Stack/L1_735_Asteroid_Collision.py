""" https://leetcode.com/problems/asteroid-collision/
A variance of monotonic stack, in this problem the "monotonic" is no collision
"""
from header import *


class Solution:
    def asteroidCollision(self, A: List[int]) -> List[int]:
        stk = []
        for i in range(len(A)):
            f = True
            while stk and A[stk[-1]] > 0 and A[i] < 0:
                if abs(A[stk[-1]]) < abs(A[i]):
                    stk.pop()
                else:
                    if abs(A[stk[-1]]) == abs(A[i]):
                        stk.pop()
                    f = False
                    break
            if f:
                stk.append(i)
        return [A[x] for x in stk]
