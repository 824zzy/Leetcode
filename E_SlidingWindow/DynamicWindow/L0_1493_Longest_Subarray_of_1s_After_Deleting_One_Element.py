""" https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
The same as 1004_Max_Consecutive_Ones_III.py

Change up to k = 1 values from 0 to 1.
Return the length - 1 of the longest (contiguous) subarray that contains only 1s.
"""
from header import *

class Solution:
    def longestSubarray(self, A: List[int]) -> int:
        i = 0
        ans = 0
        k = 1
        for j in range(len(A)):
            if A[j]==0: k -= 1
            while k<0:
                if A[i]==0: k += 1
                i += 1
            ans = max(ans, j-i)
        return ans