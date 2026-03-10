""" https://leetcode.com/problems/duplicate-zeros/
Make a forward movement to count number of zeros to arrive at the total length len(A) + zeros if not truncated.
Move backward to put in element once the pointer is within the length.
"""


class Solution:
    def duplicateZeros(self, A: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = A.count(0)
        for j in reversed(range(len(A))):
            if j + i < len(A):
                A[j + i] = A[j]
            if A[j] == 0:
                i -= 1
                if j + i < len(A):
                    A[j + i] = A[j]
