""" https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/
idea from guan: https://github.com/wisdompeak/LeetCode/blob/master/Others/995.Minimum-Number-of-K-Consecutive-Bit-Flips/995.Minimum-Number-of-K-Consecutive-Bit-Flips.cpp
"""
from header import *

class Solution:
    def minKBitFlips(self, A: List[int], k: int) -> int:
        diff = [0]*(len(A)+1)
        flips = 0
        ans = 0
        for i in range(len(A)):
            flips += diff[i]
            if (flips+A[i])%2==1: continue
            if i+k-1>=len(A): return -1
            flips += 1
            ans += 1
            diff[i+k] -= 1
        return ans