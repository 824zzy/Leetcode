""" https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/submissions/
If you can make the first x values and you have a value v, then you can make all the values ≤ v + x
"""
from header import *

class Solution:
    def getMaximumConsecutive(self, A: List[int]) -> int:
        A.sort()
        mx = 1
        for x in A:
            if mx<x:
                return mx
            mx += x
        return mx
        
        
"""
[1,3]
[1,1,1,4]
[1,4,10,3,1]
"""