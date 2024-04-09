""" https://leetcode.com/problems/find-good-days-to-rob-the-bank/
The same as 2420_Find_All_Good_Indices_L1.py

1. pre-calculate prefix and suffix array of increasing and decreasing elements counts
2. find days whose counts larger than time
"""
from header import *


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        A = [0] * len(security)
        for i in range(1, len(A)):
            if security[i - 1] >= security[i]:
                A[i] = A[i - 1] + 1

        _A = [0] * len(security)
        for i in reversed(range(len(_A) - 1)):
            if security[i] <= security[i + 1]:
                _A[i] = _A[i + 1] + 1

        ans = []
        for i in range(len(A)):
            if A[i] >= time and _A[i] >= time:
                ans.append(i)
        return ans
