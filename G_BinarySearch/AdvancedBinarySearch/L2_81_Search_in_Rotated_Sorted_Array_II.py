""" https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
If the number in the middle is less than the rightmost number, the right half is ordered;
If the middle number is greater than the rightmost number, the left half is ordered.
Else if the middle number is equal to rightmost number, the right pointer should minus one.
"""
from header import *

class Solution:
    def search(self, A: List[int], t: int) -> bool:
        def fn(m):
            if A[l]<=A[m]:
                if A[l]<=t<=A[m]:
                    return True
                else:
                    return False
            else:
                if A[m]<t<=A[r]:
                    return False
                else:
                    return True
                
        l, r = 0, len(A)-1
        while l<r:
            m = (l+r)//2
            if A[l]==A[r]: r -= 1
            elif fn(m): r = m
            else: l = m+1
        return A[l-1]==t or A[l]==t