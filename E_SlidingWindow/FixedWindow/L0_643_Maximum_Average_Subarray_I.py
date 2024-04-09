""" https://leetcode.com/problems/maximum-average-subarray-i/
fixed sliding window + simulation
"""
from header import *


class Solution:
    def findMaxAverage(self, A: List[int], k: int) -> float:
        sm = sum(A[:k])
        ans = sm / k
        for i in range(k, len(A)):
            sm += A[i]
            sm -= A[i - k]
            ans = max(ans, sm / k)
        return ans
