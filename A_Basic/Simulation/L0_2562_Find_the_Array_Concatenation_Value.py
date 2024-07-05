""" https://leetcode.com/problems/find-the-array-concatenation-value/
simulation
"""
from header import *


class Solution:
    def findTheArrayConcVal(self, A: List[int]) -> int:
        ans = 0
        while len(A) > 1:
            x = A.pop(0)
            y = A.pop()
            ans += int(str(x) + str(y))
        if A:
            return ans + A[0]
        else:
            return ans


# digit enumeration by Ox3ff


class Solution:
    def findTheArrayConcVal(self, A: List[int]) -> int:
        ans = 0
        l, r = 0, len(A) - 1
        while l < r:
            x, y = A[l], A[r]
            while y:
                x *= 10
                y //= 10
            ans += x + A[r]
            l += 1
            r -= 1
        if l == r:
            return ans + A[l]
        else:
            return ans
