""" https://leetcode.com/problems/check-if-matrix-is-x-matrix/
find diagnal by: i==j or i+j==n-1
"""


class Solution:
    def checkXMatrix(self, A: List[List[int]]) -> bool:
        n = len(A)
        for i in range(n):
            for j in range(n):
                if i == j or i == n - j - 1:
                    if A[i][j] == 0:
                        return False
                else:
                    if A[i][j] != 0:
                        return False
        return True
