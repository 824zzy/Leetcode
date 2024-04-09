""" https://leetcode.com/problems/valid-sudoku/description/
Simulate the rules
"""
from header import *


class Solution:
    def isValidSudoku(self, A: List[List[str]]) -> bool:
        # check rows
        for row in A:
            seen = [False] * 10
            for x in row:
                if x == '.':
                    continue
                x = int(x)
                if seen[x]:
                    return False
                seen[x] = True

        # check cols
        for col in zip(*A):
            seen = [False] * 10
            for x in col:
                if x == '.':
                    continue
                x = int(x)
                if seen[x]:
                    return False
                seen[x] = True

        # check sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                vals = [
                    A[ii][jj] for ii in range(
                        i,
                        i +
                        3) for jj in range(
                        j,
                        j +
                        3) if A[ii][jj] != '.']
                if len(vals) != len(set(vals)):
                    return False
        return True
