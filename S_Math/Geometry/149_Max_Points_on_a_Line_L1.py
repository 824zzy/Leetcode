""" https://leetcode.com/problems/max-points-on-a-line/
Brute force to compute every slopes, and find the one has maximum frequency
"""
from header import *

class Solution:
    def maxPoints(self, A: List[List[int]]) -> int:        
        ans = 0
        for i in range(len(A)):
            mp = Counter()
            x1, y1 = A[i]
            for j in range(len(A)):
                if i==j: continue
                x2, y2 = A[j]
                if x1==x2: mp[inf] += 1
                else:
                    mp[(y2-y1)/(x2-x1)] += 1
            ans = max(ans, 1+max(mp.values(), default=0))
        return ans