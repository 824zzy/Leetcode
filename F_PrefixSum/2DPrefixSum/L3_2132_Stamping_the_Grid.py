""" https://leetcode.com/problems/stamping-the-grid/
steal from ye15 with my comments: https://leetcode.com/problems/stamping-the-grid/discuss/1684292/Python3-prefix-sum
"""


class Solution:
    def possibleToStamp(self, A: List[List[int]], H: int, W: int) -> bool:
        # compute the 2D prefix sum of A
        m, n = len(A), len(A[0])
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = (
                    A[i][j] + prefix[i + 1][j] + prefix[i][j + 1] - prefix[i][j]
                )

        # find places where can put stamp
        canPut = [[0] * n for _ in range(m)]
        for i in range(m - H + 1):
            for j in range(n - W + 1):
                diff = (
                    prefix[i + H][j + W]
                    - prefix[i + H][j]
                    - prefix[i][j + W]
                    + prefix[i][j]
                )
                if diff == 0:
                    canPut[i][j] = 1

        # compute the 2D prefix sum of canPut
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = (
                    canPut[i][j] + prefix[i + 1][j] + prefix[i][j + 1] - prefix[i][j]
                )

        # check if all the cells can be stamped
        for i in range(m):
            ii = max(0, i - H + 1)
            for j in range(n):
                jj = max(0, j - W + 1)
                if (
                    A[i][j] == 0
                    and prefix[i + 1][j + 1]
                    - prefix[i + 1][jj]
                    - prefix[ii][j + 1]
                    + prefix[ii][jj]
                    == 0
                ):
                    return False
        return True
