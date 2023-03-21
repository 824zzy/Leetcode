""" https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/
Implement the problem description using a seen array
"""
from header import *

class Solution:
    def findScore(self, A: List[int]) -> int:
        seen = [0]*(len(A)+2)
        ans = 0
        for i, x in sorted(enumerate(A), key=lambda x: x[1]):
            if not seen[i]:
                ans += x
                seen[i] = 1
                seen[i-1] = 1
                seen[i+1] = 1
        return ans