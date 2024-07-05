""" https://leetcode.com/problems/game-of-life/
The key to in-place operation is almost always to properly code the matrix so that the info is kept.
For this problem, when we mark a cell live (i.e. 1) or dead (i.e. 0),
we can overshoot the numbers. Namely, when changing 1 to 0 we overshoot it to -1;
when changing 0 to 1, we overshoot it to 2.
"""


class Solution:
    def gameOfLife(self, A: List[List[int]]) -> None:
        D = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, 1), (1, 0), (1, -1)]
        # -1: 1==>0(live to dead), 2: 0==>1(dead to live)
        for x in range(len(A)):
            for y in range(len(A[0])):
                cnt = 0
                for dx, dy in D:
                    if (
                        0 <= x + dx < len(A)
                        and 0 <= y + dy < len(A[0])
                        and A[x + dx][y + dy] in (1, -1)
                    ):
                        cnt += 1
                # live to dead
                if A[x][y] and (cnt < 2 or cnt > 3):
                    A[x][y] = -1
                # dead to live
                elif not A[x][y] and cnt == 3:
                    A[x][y] = 2

        for i in range(len(A)):
            for j in range(len(A[0])):
                A[i][j] = int(A[i][j] > 0)
