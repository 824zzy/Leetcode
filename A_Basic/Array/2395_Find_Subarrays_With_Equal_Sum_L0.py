""" https://leetcode.com/problems/find-subarrays-with-equal-sum/
use hash set check if the two continuous subarrays have the same sum
"""
from header import * 

class Solution:
    def findSubarrays(self, A: List[int]) -> bool:
        seen = set()
        for i in range(len(A)-1):
            if A[i]+A[i+1] in seen: return True
            seen.add(A[i]+A[i+1])
        return False