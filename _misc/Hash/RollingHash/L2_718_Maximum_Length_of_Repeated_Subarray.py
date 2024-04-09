""" https://leetcode.com/problems/maximum-length-of-repeated-subarray/
binary search + rolling hash.

1. hash function: hs = hs * size + val
2. update hash: hs -= val * size ** seq_size
"""
from header import *


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        def fn(k):
            """Return True if a subarray of length k can be found in A and B."""
            seen = defaultdict(list)
            hs = 0  # rolling hash
            for i in range(len(A)):
                hs = 100 * hs + A[i]
                if i >= k - 1:
                    seen[hs].append(i)
                    hs -= A[i - (k - 1)] * 100**(k - 1)  # % 1_000_000_007

            hs = 0
            for i in range(len(B)):
                hs = 100 * hs + B[i]
                if i >= k - 1:
                    for ii in seen[hs]:
                        if A[ii - k + 1:ii + 1] == B[i - k + 1:i + 1]:
                            return True
                    hs -= B[i - (k - 1)] * 100**(k - 1)  # % 1_000_000_007
            return False

        # last True binary search
        lo, hi = 0, len(A)
        while lo < hi:
            mid = lo + hi + 1 >> 1
            if fn(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
