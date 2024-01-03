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
        prefix = 0
        for x in A:
            prefix += x
            ans |= x|prefix
        return ans

# lame solution
class Solution:
    def subsequenceSumOr(self, A: List[int]) -> int:
        pref = list(accumulate(A, initial=0))
        ans = [0]*100
        for i in range(100):
            cnt = 0
            for x in pref+A:
                if (x>>i)&1:
                    ans[i] = 1
                    break
        return sum(2**i for i in range(len(ans)) if ans[i])