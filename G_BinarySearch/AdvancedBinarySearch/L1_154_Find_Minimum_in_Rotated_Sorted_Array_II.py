""" https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
non-target binary search, use r -= 1 to deal with duplicated numbers.
"""


class Solution:
    def findMin(self, A: List[int]) -> int:
        l, r = 0, len(A) - 1
        while l < r:
            m = (l + r) // 2
            if A[m] > A[r]:
                l = m + 1
            elif A[m] < A[r]:
                r = m
            else:
                r -= 1
        return A[l]
