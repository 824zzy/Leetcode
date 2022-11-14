""" https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/description/
brute-forcely check all lcm subarrays.
Pruning: if A[j] is not a factor of k, then the lcm of the subarray is not k 
"""
from header import *

class Solution:
    def subarrayLCM(self, A: List[int], k: int) -> int:
        ans = 0
        for i in range(len(A)):
            prefix = A[i]
            for j in range(i, len(A)):
                if k%A[j]==0:
                    if lcm(prefix, A[j])==k:
                        ans += 1
                    prefix = lcm(prefix, A[j])
                else:
                    break
        return ans