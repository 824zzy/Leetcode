""" https://leetcode.com/problems/find-if-array-can-be-sorted/
string simulation to ensure:
1. Each pair in the original and sorted nums has the same bit count.
2. Each "segment" should have the same bit count. The segment has the range of [min(i, B[i][2]), max(i, B[i][2])+1].
"""

from header import *


class Solution:
    def canSortArray(self, A: List[int]) -> bool:
        A = [(x, x.bit_count(), i) for i, x in enumerate(A)]
        B = sorted(A)

        for i in range(len(A)):
            if A[i][0] == B[i][0] and A[i][2] == B[i][2]:
                continue
            if A[i][1] != B[i][1]:
                return False
            seen = set()
            for j in range(min(i, B[i][2]), max(i, B[i][2]) + 1):
                seen.add(A[j][1])
            if len(seen) != 1:
                return False
        return True


"""
1000
0100
0010
1111
11110

2,4,8,15,30
1,1,1,4,4

1,1,1,4,4
"""
"""
[8,4,2,30,15]
[1,2,3,4,5]
[3,16,8,4,2]
[75,34,30]
[174, 175, 234, 188]
[20, 6, 7, 10, 20, 6, 20]
"""
