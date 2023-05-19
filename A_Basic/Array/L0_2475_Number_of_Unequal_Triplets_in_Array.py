""" https://leetcode.com/problems/number-of-unequal-triplets-in-array/
brute force, time complexity: O(n^3)
"""
from header import *

class Solution:
    def unequalTriplets(self, A: List[int]) -> int:
        ans = 0
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                for k in range(j+1, len(A)):
                    if A[i]!=A[j] and A[j]!=A[k] and A[i]!=A[k]:
                        ans += 1
        return ans