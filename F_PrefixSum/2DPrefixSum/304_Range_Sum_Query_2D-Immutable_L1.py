""" https://leetcode.com/problems/range-sum-query-2d-immutable/
2D prefix sum template
"""
class NumMatrix:
    def __init__(self, A: List[List[int]]):
        m, n = len(A), len(A[0])
        self.prefix = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                self.prefix[i+1][j+1] = A[i][j]+self.prefix[i][j+1]+self.prefix[i+1][j]-self.prefix[i][j]

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        return self.prefix[r2+1][c2+1]-self.prefix[r2+1][c1]-self.prefix[r1][c2+1]+self.prefix[r1][c1]