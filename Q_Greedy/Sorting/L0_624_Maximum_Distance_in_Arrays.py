""" https://leetcode.com/problems/maximum-distance-in-arrays/
1. greedy sort
2. figure out two cases
"""
from header import *

class Solution:
    def maxDistance(self, A: List[List[int]]) -> int:
        mn, mx = [], []
        for i, x in enumerate(A):
            mn.append((x[0], i))
            mx.append((x[-1], i))
        mn.sort()
        mx.sort(reverse=True)
        if mn[0][1]!=mx[0][1]:
            return mx[0][0]-mn[0][0]
        else:
            return max(mx[1][0]-mn[0][0], mx[0][0]-mn[1][0])