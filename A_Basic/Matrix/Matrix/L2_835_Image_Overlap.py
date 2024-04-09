""" https://leetcode.com/problems/image-overlap/
1. generate point positions of A and B
2. use d to record patterns of sliding
"""
from header import *


class Solution:
    def largestOverlap(self, A, B):
        d = defaultdict(int)
        a = []
        b = []
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    a.append((i, j))
                if B[i][j] == 1:
                    b.append((i, j))

        ans = 0
        for t1 in a:
            for t2 in b:
                t3 = (t2[0] - t1[0], t2[1] - t1[1])
                d[t3] += 1
                ans = max(ans, d[t3])
        return ans
