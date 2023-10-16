""" https://leetcode.com/problems/majority-element/
Boyer-Moore majority voting algorithm
"""
from header import *

class Solution:
    def majorityElement(self, A: List[int]) -> int:
        cnt, cand = 0, None
        for x in A:
            if x==cand: cnt += 1
            elif cnt==0: cand = x
            else: cnt -= 1
        return cand