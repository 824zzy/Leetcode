""" https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/description/
simple matrix simulation
"""
from header import *

class Solution:
    def onesMinusZeros(self, A: List[List[int]]) -> List[List[int]]:
        onesRow, onesCol, zerosRow, zerosCol = [], [], [], []
        for r in A:
            onesRow.append(r.count(1))
            zerosRow.append(r.count(0))
        
        for c in zip(*A):
            onesCol.append(c.count(1))
            zerosCol.append(c.count(0))
        
        ans = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                ans[i][j] = onesRow[i]+onesCol[j]-zerosRow[i]-zerosCol[j]
        return ans