""" https://leetcode.com/problems/max-consecutive-ones-iii/
sliding window template: move i when k<0
"""
from header import *

class Solution:
    def longestOnes(self, A: List[int], k: int) -> int:
        i = 0
        ans = 0
        for j in range(len(A)):
            if A[j]==0: k -= 1
            while k<0:
                if A[i]==0: k += 1
                i += 1
            ans = max(ans, j-i+1)
        return ans