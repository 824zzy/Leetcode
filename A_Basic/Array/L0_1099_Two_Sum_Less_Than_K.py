""" https://leetcode.com/problems/two-sum-less-than-k/description/
brute force
"""
from header import *

class Solution:
    def twoSumLessThanK(self, A: List[int], k: int) -> int:
        ans = -1
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                if A[i]+A[j]<k:
                    ans = max(ans, A[i]+A[j])
        return ans