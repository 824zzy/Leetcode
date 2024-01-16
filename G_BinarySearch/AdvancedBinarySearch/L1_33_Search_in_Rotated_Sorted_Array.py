""" https://leetcode.com/problems/search-in-rotated-sorted-array/
binary search + categorization

There are two cases can lead to r=m:
1. When the left part is sorted and t is in the range of [A[l], A[m]].
2. When there is a twist in the left part and t is in the left part, i.e., A[l]<=t or t<=A[m].
"""
from header import *

class Solution:
    def search(self, A: List[int], t: int) -> int:
        def fn(m):
            if A[l]<=A[m]: # if left part is ordered
                # if t in left part
                if A[l]<=t<=A[m]:
                    return True
                else:
                    return False
            elif A[l]<=t or t<=A[m]: # [6]70[1]
                return True
                
            if A[m]<=A[r]: # if right part is ordered
                # if t in right part
                if A[m]<=t<=A[r]:
                    return False
                else:
                    return True
            elif A[m]<=t or t<=A[r]: # [6]70[1]
                return False
            
        l, r = 0, len(A)-1
        while l<r:
            m = (l+r)//2
            if fn(m):
                r = m
            else:
                l = m+1
        return l if l<len(A) and A[l]==t else -1