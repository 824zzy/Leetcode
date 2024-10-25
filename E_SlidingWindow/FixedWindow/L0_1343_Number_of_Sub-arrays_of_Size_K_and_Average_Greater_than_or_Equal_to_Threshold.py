""" https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
apply the fixed sliding window template
"""

from header import *


class Solution:
    def numOfSubarrays(self, A: List[int], k: int, threshold: int) -> int:
        sm = sum(A[:k])
        ans = 1 if sm >= threshold * k else 0
        for i in range(k, len(A)):
            sm -= A[i - k]
            sm += A[i]
            if sm >= threshold * k:
                ans += 1
        return ans
