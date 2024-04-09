""" https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
greedily use two pointers to:
1. calculate the maximum and sum of the distinct subarray
2. once the two pointers have different colors, update answer by sm-mx, and reset sm, mx and i.
"""
from header import *


class Solution:
    def minCost(self, S: str, T: List[int]) -> int:
        i = 0
        sm = 0
        mx = 0
        ans = 0
        for j in range(len(S)):
            while i < len(S) and S[i] == S[j]:
                sm += T[i]
                mx = max(mx, T[i])
                i += 1
            if sm - mx:
                ans += sm - mx
            sm = 0
            mx = 0
        return ans


"""
"abaac"
[1,2,3,4,5]
"abc"
[1,2,3]
"aabaa"
[1,2,3,4,1]
"""
