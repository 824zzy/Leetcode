""" https://leetcode.com/problems/minimize-maximum-of-array/
Mini-max ==> Binary Search

In binary search function, we need to check if the current value can be a valid maximum or not.
"""
from header import *

class Solution:
    def minimizeArrayValue(self, A: List[int]) -> int:
        def fn(mx):
            buffer = 0
            for x in A:
                if x<mx:
                    buffer += mx-x
                else:
                    buffer -= x-mx
                if buffer<0: return False
            return True

        # reversely check also works
        # def fn(mx):
        #     _A = A.copy()
        #     for i in reversed(range(1, len(_A))):
        #         if _A[i]>mx:
        #             _A[i-1] += _A[i]-mx
        #     return _A[0]<=mx
            
        l, r = A[0], max(A)+1
        while l<r:
            m = (l+r)//2
            if fn(m): r = m
            else: l = m + 1
        return l
    
"""
[3,7,1,6]
[1,3,5]
[10, 1]
"""