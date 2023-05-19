""" https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/
find distinct integers after reverse operations by a set
"""
from header import *

class Solution:
    def countDistinctIntegers(self, A: List[int]) -> int:
        A = set(A)
        seen = A.copy()
        for x in A:
            seen.add(int(str(x)[::-1]))
        return len(seen)