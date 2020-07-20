class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        for i, row in enumerate(A):
            if row[0]==0:
                for j in range(len(row)):
                    A[i][j] = 1 if A[i][j]==0 else 0
        for i, col in enumerate(zip(*A)):
            if col.count(0)>col.count(1):
                for j in range(len(col)):
                    A[j][i] = 0 if A[j][i]==1 else 1
        ans = 0
        for row in A:
            ans += int("".join([str(c) for c in row]), 2)
        return ans