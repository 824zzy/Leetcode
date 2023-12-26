""" https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/
reading comprehension:
1. sort the array
2. enumerate the array and check if the prefix sum is less than A[i]
"""
from header import *

class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        prefix = list(accumulate(A))
        for i in reversed(range(2, len(A))):
            if prefix[i-1]>A[i]:
                return prefix[i]
        return -1
        
        
"""
[5,5,5]
[1,12,1,2,5,50,3]
[5,5,50]
"""