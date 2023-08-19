""" https://leetcode.com/problems/search-in-rotated-sorted-array/
Binary search with special condition.
There are two cases can lead to r=m:
1. When the left part is sorted and t is in the range of [A[l], A[m]].
2. When there is a twist in the left part and t is in the left part, i.e., A[l]<=t or t<=A[m].
"""
from header import *

class Solution:
    def search(self, A: List[int],t: int) -> int:
        l, r = 0, len(A)-1
        while l<r:
            m = (l+r)//2
            if (A[l]<=t<=A[m]) or (A[l]>A[m] and (A[l]<=t or t<=A[m])):
                r = m
            else:
                l = m+1
        return l if A[l]==t else -1