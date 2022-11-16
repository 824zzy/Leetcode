""" https://leetcode.com/problems/find-peak-element/description/
the sentinel is to check if A[mid] is the peak (i.e. A[mid]<A[mid+1])
"""
from header import *

class Solution:
    def findPeakElement(self, A: List[int]) -> int:
        def fn(x):
            if A[x]<A[x+1]:
                return False
            else:
                return True

        l, r = 0, len(A)-1
        while l<r:
            m = (l+r)//2
            if fn(m): r = m
            else: l = m+1
        return l