""" https://leetcode.com/problems/search-in-rotated-sorted-array/
Define l and r as the lower and upper bound of the array index that we are checking. 
Iteratively divide the array into two pieces, and discard the one that target is not in.
"""
from header import *

class Solution:
    def search(self, A: List[int], t: int) -> int:
        def fn(m):
            if not 0<=l<=m<=r<len(A): return False
            if A[l]<=A[m]:
                if A[l]<=t<A[m]: return True
                else: return False
            else:
                if A[m]<t<=A[r]: return False
                else: return True
            
        l, r = 0, len(A)-1
        
        while l<r:
            m = (l+r)//2
            if A[m]==t: return m
            if fn(m): r = m
            else: l = m+1
                
        if A[l]==t: return l
        else: return -1