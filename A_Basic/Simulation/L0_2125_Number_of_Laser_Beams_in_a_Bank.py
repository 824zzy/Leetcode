""" https://leetcode.com/problems/number-of-laser-beams-in-a-bank/
simulate laser beam row by row
"""
from header import *

class Solution:
    def numberOfBeams(self, A: List[str]) -> int:
        ans = 0
        pre = 0
        for i in range(len(A)):
            if A[i].count('1'):
                ans += pre * A[i].count('1')
                pre = A[i].count('1')
        return ans