""" https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/
Observation: since bitwise AND of maximum and any other number will make the result smaller.

So find longest consecutive subarray of all maximum by groupby.
"""
from header import *

class Solution:
    def longestSubarray(self, A: List[int]) -> int:
        mx = max(A)
        A = [[k, len(list(v))] for k, v in groupby(A)]
        ans = 0
        for k, v in A:
            if k==mx:
                ans = max(v, ans)
        return ans