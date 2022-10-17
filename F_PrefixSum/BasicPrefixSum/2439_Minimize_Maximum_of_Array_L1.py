""" https://leetcode.com/problems/minimize-maximum-of-array/
At index i, greedily compute the maximum average of the prefix sum A[i]
"""
from header import *

class Solution:
    def minimizeArrayValue(self, A: List[int]) -> int:
        sm = 0
        ans = 0
        for i in range(len(A)):
            sm += A[i]
            ans = max(ans, ceil(sm/(i+1)))
        return ans
    
"""
[3,7,1,6]
[1,3,5]
[10, 1]
"""