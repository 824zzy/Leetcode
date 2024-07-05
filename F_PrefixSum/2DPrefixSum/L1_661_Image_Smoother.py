""" https://leetcode.com/problems/image-smoother/
simulation
"""
from header import *

# 2D prefix sum


class Solution:
    def imageSmoother(self, A: List[List[int]]) -> List[List[int]]:
        m, n = len(A), len(A[0])
        prefix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = (
                    A[i][j] + prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j]
                )

        for i in range(m):
            for j in range(n):
                x1, y1 = max(0, i - 1), max(0, j - 1)
                x2, y2 = min(m - 1, i + 1), min(n - 1, j + 1)
                cnt = (x2 - x1 + 1) * (y2 - y1 + 1)
                sm = (
                    prefix[x2 + 1][y2 + 1]
                    - prefix[x1][y2 + 1]
                    - prefix[x2 + 1][y1]
                    + prefix[x1][y1]
                )
                A[i][j] = sm // cnt
        return A


# simulation


class Solution:
    def imageSmoother(self, A: List[List[int]]) -> List[List[int]]:
        ans = deepcopy(A)
        m, n = len(A), len(A[0])
        for i in range(m):
            for j in range(n):
                sm = 0
                cnt = 0
                for ii in range(i - 1, i + 2):
                    for jj in range(j - 1, j + 2):
                        if 0 <= ii < m and 0 <= jj < n:
                            sm += A[ii][jj]
                            cnt += 1
                ans[i][j] = sm // cnt
        return ans


"""
[[1,1,1],[1,0,1],[1,1,1]]
[[100,200,100],[200,50,200],[100,200,100]]
[[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
"""
