""" https://leetcode.com/problems/build-a-matrix-with-conditions/
use topological sort to find the order of rows and columns,
then build a matrix with those orders
"""
from header import *


class Solution:
    def buildMatrix(
        self, k: int, R: List[List[int]], C: List[List[int]]
    ) -> List[List[int]]:
        def topo(A):
            e = defaultdict(list)
            inD = [0] * (k + 1)
            for i, j in A:
                e[i].append(j)
                inD[j] += 1

            Q = [i for i, d in enumerate(inD) if d == 0 and i != 0]
            _A = []
            while Q:
                i = Q.pop(0)
                _A.append(i)
                for j in e[i]:
                    inD[j] -= 1
                    if not inD[j]:
                        Q.append(j)

            if sum(inD):
                return []
            else:
                return _A

        R = topo(R)
        C = topo(C)
        if not R or not C:
            return []
        R = {x: i for i, x in enumerate(R)}
        C = {x: i for i, x in enumerate(C)}
        ans = [[0 for _ in range(k)] for _ in range(k)]
        for x in range(1, k + 1):
            ans[R[x]][C[x]] = x
        return ans
