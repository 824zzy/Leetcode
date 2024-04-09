""" https://leetcode.com/problems/remove-duplicates-from-sorted-array/
copy A[j] to A[i] if A[j] is not seen yet
"""
from header import *


class Solution:
    def removeDuplicates(self, A: List[int]) -> int:
        i = 0
        for j in range(len(A)):
            if i == 0 or A[j] != A[i - 1]:
                A[i] = A[j]
                i += 1
        return i

# suboptimal solution


class Solution:
    def removeDuplicates(self, A: List[int]) -> int:
        seen = set()
        i = 0
        for j in range(len(A)):
            if A[j] not in seen:
                A[i] = A[j]
                seen.add(A[j])
                i += 1
        return i
