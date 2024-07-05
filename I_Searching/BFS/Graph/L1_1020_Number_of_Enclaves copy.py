""" https://leetcode.com/problems/number-of-enclaves/
1. start from edge cells and go inwards by bfs and label them as 0
2. find the remained 1's cells
"""
from header import *


class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(x, y):
            Q = [(x, y)]
            while Q:
                x, y = Q.pop(0)
                A[x][y] = 0
                for dx, dy in D:
                    if (
                        0 <= x + dx < len(A)
                        and 0 <= y + dy < len(A[0])
                        and A[x + dx][y + dy] == 1
                    ):
                        A[x + dx][y + dy] = 0
                        Q.append((x + dx, y + dy))

        for i in range(len(A)):
            for j in range(len(A[0])):
                if (not i or not j or i == len(A) - 1 or j == len(A[0]) - 1) and A[i][
                    j
                ] == 1:
                    bfs(i, j)

        ans = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    ans += 1
        return ans
