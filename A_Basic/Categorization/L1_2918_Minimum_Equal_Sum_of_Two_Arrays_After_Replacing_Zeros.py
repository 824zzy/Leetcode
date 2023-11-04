""" https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/
categorization:
Case1: A cannot become B
    a0==0 and b+b0>a ==> -1
Case2: B cannot become A
    b0==0 and a+a0>b
Case3: both array has zero:
    max(a+a0, b+b0)
"""
from header import *

class Solution:
    def minSum(self, A: List[int], B: List[int]) -> int:
        a, b = sum(A), sum(B)
        a0, b0 = A.count(0), B.count(0)
        if (a0==0 and b+b0>a) or (b0==0 and a+a0>b):
            return -1
        return max(a+a0, b+b0)
        
        
"""
[3,2,0,1,0]
[6,5,0]
[2,0,2,0]
[1,4]
"""