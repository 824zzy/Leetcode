""" https://leetcode.com/problems/bag-of-tokens/
1. sort the tokens first
2. greedily play the left token face up and right token face down
"""
from header import *


class Solution:
    def bagOfTokensScore(self, A: List[int], p: int) -> int:
        A.sort()
        res = 0
        l, r = 0, len(A) - 1
        while l <= r:
            while l <= r and p >= A[l]:
                p -= A[l]
                l += 1
                res += 1
            if l < r and res:
                p += A[r]
                r -= 1
                res -= 1
            else:
                break
        return res
