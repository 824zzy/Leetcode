""" https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/
Sweep through A and check the longest arithmetic subsequence ending at current value.
"""
from header import *

class Solution:
    def longestSubsequence(self, A: List[int], dif: int) -> int:
        seen = Counter()
        for x in A:
            seen[x] = seen[x-dif]+1
        return max(seen.values())