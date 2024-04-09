""" https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/
1. greedy sort
2. group and reassign index
"""
from header import *


class Solution:
    def lexicographicallySmallestArray(
            self, A: List[int], limit: int) -> List[int]:
        ans = A.copy()
        A = [(x, i) for i, x in enumerate(A)]
        A.append((inf, inf))
        A.sort()

        grp = []
        for i in range(len(A)):
            if i and A[i][0] - A[i - 1][0] > limit:
                for x, y in enumerate(sorted(x for _, x in grp)):
                    ans[y] = grp[x][0]
                grp = []
            grp.append(A[i])
        return ans


"""
[1,5,3,9,8]
2
[1,7,6,18,2,1]
3
[1,7,28,19,10]
3
[3,2,1]
100000
"""
