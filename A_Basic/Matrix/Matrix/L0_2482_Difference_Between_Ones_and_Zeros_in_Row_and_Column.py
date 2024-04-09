""" https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/
observation:
    diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj
               = (onesRowi - zerosRowi) + (onesColj - zerosColj)
matrix simulation
"""
from header import *


class Solution:
    def onesMinusZeros(self, A: List[List[int]]) -> List[List[int]]:
        row = defaultdict(int)
        col = defaultdict(int)
        for i, x in enumerate(A):
            row[i] = x.count(1) - x.count(0)
        for i, c in enumerate(zip(*A)):
            col[i] = c.count(1) - c.count(0)

        for i in range(len(A)):
            for j in range(len(A[0])):
                A[i][j] = row[i] + col[j]
        return A
