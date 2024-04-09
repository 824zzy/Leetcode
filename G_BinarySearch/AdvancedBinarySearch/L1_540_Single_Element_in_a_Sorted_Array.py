""" https://leetcode.com/problems/single-element-in-a-sorted-array/
for m, find if there enough pairs till m by checking previous/next element
"""
from header import *


class Solution:
    def singleNonDuplicate(self, A: List[int]) -> int:
        def enough(m):
            if (m % 2 == 0 and A[m] == A[m + 1]) or \
               (m % 2 == 1 and A[m] == A[m - 1]):
                return True
            else:
                return False

        l, r = 0, len(A) - 1
        while l < r:
            m = (l + r) // 2
            if enough(m):
                l = m + 1
            else:
                r = m
        return A[l]

# smart solution using XOR


class Solution:
    def singleNonDuplicate(self, A: List[int]) -> int:
        def enough(m):
            """ explanation of A[m]==A[m^1]
            A[m] and A[m^1] is for pairing indexes of A(e.g. {0, 1}, {2, 3}, {4, 5})
            """
            if A[m] == A[m ^ 1]:
                return True
            else:
                return False

        l, r = 0, len(A) - 1
        while l < r:
            m = (l + r) // 2
            if enough(m):
                l = m + 1
            else:
                r = m
        return A[l]
