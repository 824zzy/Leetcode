""" https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/
simulation
"""
from header import *


class Solution:
    def missingInteger(self, A: List[int]) -> int:
        # find longest increasing prefix
        pre = A[0]
        for i in range(1, len(A)):
            if A[i] - A[i - 1] != 1:
                break
            pre += A[i]
        # find the missing smallest integer
        S = set(A)
        while pre in S:
            pre += 1
        return pre


"""
[1,2,3,2,5]
[3,4,5,1,12,14,13]
[46,8,2,4,1,4,10,2,4,10,2,5,7,3,1]
"""
