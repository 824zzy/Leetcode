""" https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/
1. enumerate on index i
2. maintain a sorted list of A[i-x:i] and use bisect to find the closest element to A[i]
"""
from header import *


class Solution:
    def minAbsoluteDifference(self, A: List[int], x: int) -> int:
        sl = []
        ans = inf
        for i in range(x, len(A)):
            insort(sl, A[i - x])
            j = bisect_left(sl, A[i])
            ans = min(ans, abs(A[i] - sl[min(j, len(sl) - 1)]),
                      abs(A[i] - sl[max(j - 1, 0)]))
        return ans


"""
[4,3,2,4]
2
[5,3,2,10,15]
1
[1,2,3,4]
3
[14,111,16]
1
"""
