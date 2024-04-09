""" https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/
idea learned from https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/discuss/4304840/Sort-Queries-vs.-Exponential-Monostack

Observation:
1. when x==y or A[x]<A[y], the answer must be y
2. use monotonic stack to find the leftmost valid answer on the right of y.
"""
from header import *


class Solution:
    def leftmostBuildingQueries(
            self, A: List[int], Q: List[List[int]]) -> List[int]:
        # next greater on the right
        R = [len(A)] * len(A)
        stk = []
        for i in range(len(A)):
            while stk and A[stk[-1]] <= A[i]:
                R[stk.pop()] = i
            stk.append(i)

        ans = [-1] * len(Q)
        for i, (x, y) in enumerate(Q):
            x, y = min(x, y), max(x, y)
            if x == y or A[x] < A[y]:  # cases don't need monotonic stack
                ans[i] = y
            elif R[x] == len(A):  # edge case
                continue
            else:  # hop until find the valid index
                while R[y] < len(R) and A[R[y]] < A[x]:
                    y = R[y]
                if R[y] < len(R) and A[R[y]] > A[x]:
                    ans[i] = R[y]
        return ans


"""
[6,4,8,5,2,7]
[[0,1],[0,3],[2,4],[3,4],[2,2]]
[5,3,8,2,6,1,4,6]
[[0,7],[3,5],[5,2],[3,0],[1,6]]
[1,2,1,2,1,2]
[[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[1,0],[1,1],[1,2],[1,3],[1,4],[1,5],[2,0],[2,1],[2,2],[2,3],[2,4],[2,5],[3,0],[3,1],[3,2],[3,3],[3,4],[3,5],[4,0],[4,1],[4,2],[4,3],[4,4],[4,5],[5,0],[5,1],[5,2],[5,3],[5,4],[5,5]]
"""
