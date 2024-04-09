""" https://leetcode.com/problems/valid-mountain-array/
find left most and right most peak
"""


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        i, j = 0, len(A) - 1
        while i < n and A[i] < A[i + 1]:
            i += 1
        while j > 0 and A[j - 1] > A[j]:
            j -= 1
        return 0 < i == j < len(A)
