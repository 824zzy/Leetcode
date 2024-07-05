""" https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/
Note that it is not dp problem, instead use two pointer to find the count of subsequence
"""
from header import *


class Solution:
    def numSubseq(self, A: List[int], target: int) -> int:
        A.sort()
        ans = 0
        i, j = 0, len(A) - 1
        while i <= j:
            if A[i] + A[j] > target:
                j -= 1
            else:
                ans += pow(2, j - i, 10 ** 9 + 7)
                i += 1
        return ans % (10 ** 9 + 7)
