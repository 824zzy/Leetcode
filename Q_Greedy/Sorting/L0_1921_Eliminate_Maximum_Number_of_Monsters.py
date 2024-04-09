""" https://leetcode.com/problems/eliminate-maximum-number-of-monsters/
greedy sort + two pointers
"""
from header import *


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        A = sorted([x / y for x, y in zip(dist, speed)])
        i = 0
        for j in A:
            if i >= j:
                return i
            i += 1
        return len(A)


"""
[1,3,4]
[1,1,1]
[1,1,2,3]
[1,1,1,1]
[3,2,4]
[5,3,2]
[2]
[1]
"""
