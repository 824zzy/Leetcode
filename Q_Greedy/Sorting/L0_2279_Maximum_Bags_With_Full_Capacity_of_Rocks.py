""" https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/
sort the capacity and rocks by difference, then greedily assign additional rocks
"""
from header import *

class Solution:
    def maximumBags(self, C: List[int], R: List[int], x: int) -> int:
        A = [0] * len(C)
        for i, (c, r) in enumerate(zip(C, R)):
            A[i] = c-r
        A.sort()
        
        ans = 0
        for i in range(len(A)):
            if x-A[i]>=0: 
                ans += 1
                x -= A[i]
            else:
                break
        return ans