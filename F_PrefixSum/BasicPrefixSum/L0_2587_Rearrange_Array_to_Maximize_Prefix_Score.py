""" https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score/
greedily sort the array in decreasing order for maximize prefix score
"""
from header import *

class Solution:
    def maxScore(self, A: List[int]) -> int:
        A.sort(reverse=True)
        A = list(accumulate(A))
        ans = 0
        for i in range(len(A)):
            if A[i]>0: 
                ans += 1
        return ans