""" https://leetcode.com/problems/find-common-elements-between-two-arrays/
compute intersection and count frequency
"""
from header import *

class Solution:
    def findIntersectionValues(self, A: List[int], B: List[int]) -> List[int]:
        x = set(A)&set(B)
        return [sum(A.count(xx) for xx in x), sum(B.count(xx) for xx in x)]