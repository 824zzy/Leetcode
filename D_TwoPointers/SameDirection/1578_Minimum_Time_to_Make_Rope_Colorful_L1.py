""" https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
greedily use two pointers to:
1. calculate the maximum and sum of the distinct subarray
2. once the two pointers have different colors, update answer by sm-mx, and reset sm, mx and i.
"""
from header import *

class Solution:
    def minCost(self, A: str, T: List[int]) -> int:
        i = 0
        ans = 0
        mx = -inf
        sm = 0
        for j in range(len(A)):
            if A[i]!=A[j]:
                ans += sm-mx
                sm = 0
                mx = -inf
                i = j
            sm += T[j]
            mx = max(mx, T[j])
        return ans+(sm-mx)
            
            
                
            
"""
"abaac"
[1,2,3,4,5]
"abc"
[1,2,3]
"aabaa"
[1,2,3,4,1]
"""