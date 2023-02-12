""" https://leetcode.com/problems/find-the-array-concatenation-value/
simulation
"""
from header import *

class Solution:
    def findTheArrayConcVal(self, A: List[int]) -> int:
        ans = 0
        while len(A)>1:
            x = A.pop(0)
            y = A.pop()
            ans += int(str(x)+str(y))
        if A: return ans+A[0]
        else: return ans