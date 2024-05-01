""" https://leetcode.com/problems/bitwise-or-of-all-subsequence-sums/
The set bit of the final result has two possible sources
1. set bit in one of an original number;
2. set bit as a result of a subsequence sum.

For the 2nd source where the set bit is carried over from lower bits, you can always get the it from a prefix sum.
"""
from header import *


class Solution:
    def subsequenceSumOr(self, A: List[int]) -> int:
        ans = 0
        presum = 0
        for x in A:
            # first source
            ans |= x
            # second source
            presum += x
            ans |= presum
        return ans
