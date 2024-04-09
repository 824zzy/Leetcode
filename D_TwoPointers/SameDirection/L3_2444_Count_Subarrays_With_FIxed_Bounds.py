""" https://leetcode.com/problems/count-subarrays-with-fixed-bounds/
TODO: learn from lee: https://leetcode.com/problems/count-subarrays-with-fixed-bounds/discuss/2708099/JavaC%2B%2BPython-Sliding-Window-with-Explanation
"""
from header import *


class Solution:
    def countSubarrays(self, A: List[int], minK: int, maxK: int) -> int:
        ans = 0
        imin = imax = ibad = -1
        for j, x in enumerate(A):
            if not minK <= x <= maxK:
                ibad = j
            if x == minK:
                imin = j
            if x == maxK:
                imax = j
            ans += max(0, min(imin, imax) - ibad)
        return ans
