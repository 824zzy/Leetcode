""" https://leetcode.com/problems/minimum-average-difference/
basic usage of prefix sum, note that the answer is index rather than value!

add -0.00001 to denominator to avoid overflow
"""
from header import *


class Solution:
    def minimumAverageDifference(self, A: List[int]) -> int:
        pre = list(accumulate(A, initial=0))
        suf = list(accumulate(A[::-1], initial=0))[::-1]
        ans = []
        for i in range(1, len(A) + 1):
            ans.append(abs(pre[i] // i - suf[i] // (len(A) - i - 0.00001)))
        return ans.index(min(ans))
