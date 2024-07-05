""" https://leetcode.com/problems/toeplitz-matrix/

"""
from header import *

# save all the diagonals in a dictionary


class Solution:
    def isToeplitzMatrix(self, A: List[List[int]]) -> bool:
        cnt = defaultdict(list)
        for i in range(len(A)):
            for j in range(len(A[0])):
                cnt[i - j].append(A[i][j])

        for k, v in cnt.items():
            if len(set(v)) != 1:
                return False
        return True


# check the Toeplitz property on the fly


class Solution:
    def isToeplitzMatrix(self, m):
        for i in range(len(m) - 1):
            for j in range(len(m[0]) - 1):
                if m[i][j] != m[i + 1][j + 1]:
                    return False
        return True


"""
[[1,2,3,4],[5,1,2,3],[9,5,1,2]]
[[1,2],[2,2]]
[[36,59,71,15,26,82,87],[56,36,59,71,15,26,82],[15,0,36,59,71,15,26]]
"""
