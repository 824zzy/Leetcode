"""
Prefix sum raw of matrix
"""
class NumMatrix:
    def __init__(self, A: List[List[int]]):
        self.P = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
        for i in range(len(A)):
            pre = 0
            for j in range(len(A[0])):
                pre += A[i][j]
                self.P[i][j] = pre
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for r in range(row1, row2+1):
            if col1-1>=0: ans += self.P[r][col2]-self.P[r][col1-1]
            else: ans += self.P[r][col2]
        return ans