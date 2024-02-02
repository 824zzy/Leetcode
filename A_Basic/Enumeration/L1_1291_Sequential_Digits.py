""" https://leetcode.com/problems/sequential-digits/
enumerate all possible answers from small to large
"""
from header import *

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        for i in range(1, 10):
            cand = i
            for j in range(i+1, 10):
                cand = cand*10+j
                if low<=cand<=high:
                    ans.append(cand)
        return sorted(ans)