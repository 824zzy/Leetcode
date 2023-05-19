""" https://leetcode.com/problems/count-strictly-increasing-subarrays/
1. greedily find the length of longest increasing subarrays at each indexes
2. sum the length up
"""
from header import *

class Solution:
    def countSubarrays(self, A: List[int]) -> int:
        prefix_inc = [1]*len(A)
        for i in range(1, len(A)):
            if A[i]>A[i-1]:
                prefix_inc[i] = prefix_inc[i-1]+1
        return sum(prefix_inc)
"""
[1,2,5,4,4,6] ==> [1,2,3,1,1,2]
"""