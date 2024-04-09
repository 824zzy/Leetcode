""" https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/
1. greedy sort by start time
2. knapsack + binary search

1 <= k * events.length <= 106 ==> TC: O(k*n*logn)
"""
from header import *


class Solution:
    def maxValue(self, A: List[List[int]], k: int) -> int:
        A.sort()
        starts = [i for i, _, _ in A]

        @cache
        def fn(i, k):
            if i == len(A) or k == 0:
                return 0
            ii = bisect_left(starts, A[i][1] + 1)
            return max(fn(i + 1, k), A[i][2] + fn(ii, k - 1))

        return fn(0, k)
