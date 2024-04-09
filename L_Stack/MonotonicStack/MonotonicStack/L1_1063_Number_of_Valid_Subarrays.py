""" https://leetcode.com/problems/number-of-valid-subarrays/
1. find the next smaller element on the right
2. for each element, the number of valid subarrays is the distance between it and the next smaller element on the right
"""
from header import *


class Solution:
    def validSubarrays(self, A: List[int]) -> int:
        # next smaller on the right
        R = [len(A)] * len(A)
        stk = []
        for i in range(len(A)):
            while stk and A[stk[-1]] > A[i]:
                R[stk.pop()] = i
            stk.append(i)

        ans = 0
        for i, j in enumerate(R):
            ans += j - i
        return ans
