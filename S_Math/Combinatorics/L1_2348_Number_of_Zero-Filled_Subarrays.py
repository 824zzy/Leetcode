""" https://leetcode.com/problems/number-of-zero-filled-subarrays/
1. Use groupby rather than two pointers to count continuous 0's
2. Then pray for Gaussian for final answer :)
"""
from header import *


class Solution:
    def zeroFilledSubarray(self, A: List[int]) -> int:
        ans = 0
        for k, v in groupby(A):
            if k == 0:
                cnt = len(list(v))
                ans += cnt * (cnt + 1) // 2
        return ans


# or solve it with two pointers
class Solution:
    def zeroFilledSubarray(self, A: List[int]) -> int:
        cnt = 0
        ans = 0
        for j in range(len(A)):
            if A[j]:
                cnt = 0
            else:
                cnt += 1
            ans += cnt
        return ans
