""" https://leetcode.com/problems/max-consecutive-ones/
find consecutive ones using groupby
"""
from header import *

class Solution:
    def findMaxConsecutiveOnes(self, A: List[int]) -> int:
        return max([len(list(v)) for k, v in groupby(A) if k==1], default=0)