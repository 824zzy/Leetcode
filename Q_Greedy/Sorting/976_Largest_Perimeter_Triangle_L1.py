""" https://leetcode.com/problems/largest-perimeter-triangle/
1. Sort the array. 
2. For any cc in the array, we choose the largest possible a≤b≤c
"""
from header import *

class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        for i in range(len(A)-2):
            if A[i]<A[i+1]+A[i+2]:
                return A[i]+A[i+1]+A[i+2]
        return 0
        
        
"""
[2,2,1]
[3,6,2,3]
"""