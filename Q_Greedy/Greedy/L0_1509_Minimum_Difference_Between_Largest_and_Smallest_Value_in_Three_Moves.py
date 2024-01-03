""" https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/
greedily enumerate all possible cases
"""
from header import *

class Solution:
    def minDifference(self, A: List[int]) -> int:
        if len(A)<=4: return 0
        A.sort()
        ans = inf
        for i in range(4):
            ans = min(ans, A[-4+i]-A[i])
        return ans
    
    
"""
[5,3,2,4]
[1,5,0,10,14]
[3,100,20]
[1,2,3,4,5,67,123,4512,5125,1231]
[6,6,0,1,1,4,6]
[82,81,95,75,20]
"""