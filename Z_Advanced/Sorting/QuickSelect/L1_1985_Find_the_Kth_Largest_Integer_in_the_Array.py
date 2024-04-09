""" https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/
1. convert array elements to int
2. use quick select to find kth largest element
"""


class Solution:
    def kthLargestNumber(self, A: List[str], k: int) -> str:
        A = list(map(int, A))

        def partition(l, r):
            """Return partition of A[l:r]."""
            i, j = l + 1, r - 1
            while i <= j:
                if A[i] < A[l]:
                    i += 1
                elif A[j] > A[l]:
                    j -= 1
                else:
                    A[i], A[j] = A[j], A[i]
                    i, j = i + 1, j - 1
            A[l], A[j] = A[j], A[l]
            return j

        shuffle(A)
        l, r = 0, len(A)
        while True:
            m = partition(l, r)
            if m + k < len(A):
                l = m + 1
            elif m + k == len(A):
                return str(A[m])
            else:
                r = m
