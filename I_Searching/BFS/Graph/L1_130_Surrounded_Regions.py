""" https://leetcode.com/problems/surrounded-regions/
1. flood fill Os from the boundary with a sentinel # to mark that this O is not surrounded.
2. traverse the board and replace O with X and # with O.
"""


class Solution:
    def solve(self, A: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M, N = len(A), len(A[0])
        D = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(x, y):
            if A[x][y] != "O":
                return
            A[x][y] = "#"
            for dx, dy in D:
                if 0 <= x + dx < M and 0 <= y + dy < N:
                    dfs(x + dx, y + dy)

        for i in range(M):
            dfs(i, 0)
            dfs(i, N - 1)

        for j in range(N):
            dfs(0, j)
            dfs(M - 1, j)

        for i in range(M):
            for j in range(N):
                if A[i][j] == "#":
                    A[i][j] = "O"
                elif A[i][j] == "O":
                    A[i][j] = "X"
