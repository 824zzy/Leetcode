""" https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
"""
from header import *

class Solution:
    def findSpecialInteger(self, A: List[int]) -> int:
        t = len(A)//4
        cnt = 0
        for i in range(len(A)):
            if i and A[i]!=A[i-1]:
                cnt = 1
            else:
                cnt += 1
            if cnt>t:
                return A[i]