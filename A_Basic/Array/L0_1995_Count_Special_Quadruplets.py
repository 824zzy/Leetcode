""" https://leetcode.com/problems/count-special-quadruplets/
brute force search quadruplets
"""
from header import *


class Solution:
    def countQuadruplets(self, A: List[int]) -> int:
        ans = 0
        for i in range(len(A) - 3):
            for j in range(i + 1, len(A) - 2):
                for k in range(j + 1, len(A) - 1):
                    for l in range(k + 1, len(A)):
                        if A[i] + A[j] + A[k] == A[l]:
                            ans += 1
        return ans
