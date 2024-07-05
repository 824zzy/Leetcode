""" https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/
Apply union find template

1. sort logs by time
2. union find to merge two people
3. return time when n==1
"""
from header import *


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        A = list(range(n + 1))

        def find(x):
            if A[x] != x:
                A[x] = find(A[x])
            return A[x]

        def union(x, y):
            xx, yy = find(x), find(y)
            if xx == yy:
                return False
            A[xx] = yy
            return True

        for t, x, y in logs:
            if union(x, y):
                n -= 1
            if n == 1:
                return t
        return -1
