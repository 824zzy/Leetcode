""" https://leetcode.com/problems/arithmetic-subarrays/
zipping+sorting
"""
from header import *


class Solution:
    def checkArithmeticSubarrays(
            self,
            A: List[int],
            l: List[int],
            r: List[int]) -> List[bool]:
        def fn(A):
            A.sort()
            for i in range(1, len(A) - 1):
                if A[i] - A[i - 1] != A[i + 1] - A[i]:
                    return False
            return True

        Q = list(zip(l, r))
        ans = []
        for i, j in Q:
            if fn(A[i:j + 1]):
                ans.append(True)
            else:
                ans.append(False)
        return ans
