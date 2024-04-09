""" https://leetcode.com/problems/minimum-common-value/
multiple solutions:
1. binary search: O(nlogn)
2. set intersection: O(n)
3. two pointers: O(n)
"""
from header import *


class Solution:
    def getCommon(self, A: List[int], B: List[int]) -> int:
        for x in A:
            i = bisect_left(B, x)
            if i < len(B) and B[i] == x:
                return x
        return -1


class Solution:
    def getCommon(self, A: List[int], B: List[int]) -> int:
        return min(set(A) & set(B), default=-1)


class Solution:
    def getCommon(self, A: List[int], B: List[int]) -> int:
        l, r = 0, 0
        while l < len(A) and r < len(B):
            if A[l] == B[r]:
                return A[l]
            if A[l] < B[r]:
                l += 1
            else:
                r += 1
        return -1


"""
[1,2,3]
[2,4]
[1,2,3,6]
[2,3,4,5]
[3,5]
[2]
"""
