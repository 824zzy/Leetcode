""" https://leetcode.com/problems/score-after-flipping-matrix/
1. flip row if A[i][0]==0
2. flip column if 0s are more then 1s
3. convert row to numbers and sum them up
"""


class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        # flip row if A[i][0]==0
        for i in range(len(A)):
            if A[i][0] == 0:
                for j in range(len(A[0])):
                    A[i][j] = 0 if A[i][j] == 1 else 1
        # flip column if 0s are more then 1s
        for j, col in enumerate(zip(*A)):
            if col.count(0) > col.count(1):
                for i in range(len(A)):
                    A[i][j] = 0 if A[i][j] == 1 else 1
        # convert row to numbers and sum them up
        return sum(int(''.join(map(str, row)), 2) for row in A)
