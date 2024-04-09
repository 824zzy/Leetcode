""" https://leetcode.com/problems/minimum-replacements-to-sort-the-array/
greedily update upper bound reversely
"""
from header import *


class Solution:
    def minimumReplacement(self, A: List[int]) -> int:
        n = len(A)
        ans = 0
        upper = A[-1]
        for i in reversed(range(n - 1)):
            if A[i] % upper == 0:
                k = A[i] // upper
                ans += k - 1
            else:
                k = A[i] // upper + 1
                ans += k - 1
                upper = A[i] // k
        return ans


"""
[3,9,3]
[3,8,3]
[3,7,3]
"""
"""
[3,7,3]
[3,4,3,3]
[3,2,2,3,3]
[1,2,2,2,3,3]
"""
