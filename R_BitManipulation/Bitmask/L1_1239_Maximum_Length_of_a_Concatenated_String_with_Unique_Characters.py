""" https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
use bitmask to represent the string and "or" operation to a `seen` set for finding out how many different characters in a mask
"""
from header import *


class Solution:
    def maxLength(self, A: List[str]) -> int:
        A = [set(x) for x in A if len(x) == len(set(x))]
        N = len(A)
        ans = 0
        for mask in range(1 << N):
            seen = set()
            flag = True
            for i in range(N):
                if flag and mask & (1 << i):
                    if seen & A[i]:
                        flag = False
                        break
                    seen |= A[i]
            if flag:
                ans = max(ans, len(seen))
        return ans
