""" https://leetcode.com/problems/find-k-closest-elements/
find idx by bisect_left and use two pointers to find the k closest elements
"""
from header import *


class Solution:
    def findClosestElements(self, A: List[int], k: int, x: int) -> List[int]:
        idx = bisect_left(A, x)

        l, r = idx - 1, idx
        L, R = [], []
        for _ in range(k):
            if (l >= 0 and r < len(A) and abs(A[l] - x) <= abs(A[r] - x)) or r >= len(
                A
            ):
                L.append(A[l])
                l -= 1
            else:
                R.append(A[r])
                r += 1
        return L[::-1] + R
