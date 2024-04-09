""" https://leetcode.com/problems/longest-nice-subarray/
"""
from header import *

# optimal solution using bit manipulation


class Solution:
    def longestNiceSubarray(self, A: List[int]) -> int:
        seen = 0
        i = 0
        ans = 0

        for j in range(len(A)):
            while seen & A[j]:
                seen ^= A[i]
                i += 1
            seen |= A[j]
            ans = max(ans, j - i + 1)
        return ans

# sub-optimal solution using hash table


class Solution:
    def longestNiceSubarray(self, A: List[int]) -> int:
        seen = [0] * 32
        i = 0
        ans = 0

        for j in range(len(A)):
            for ii in range(32):
                if A[j] & (1 << ii):
                    seen[ii] += 1
            while any(x > 1 for x in seen):
                for ii in range(32):
                    if A[i] & (1 << ii):
                        seen[ii] -= 1
                i += 1
            ans = max(ans, j - i + 1)
        return ans
