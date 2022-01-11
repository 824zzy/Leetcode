""" https://leetcode.com/problems/stamping-the-grid/
steal from lee: https://leetcode.com/problems/stamping-the-grid/discuss/1675412/JavaC%2B%2BPython-Calulate-the-sub-matrix-sum-twice
"""
class Solution:
    def possibleToStamp(self, M, h, w):
        m, n = len(M), len(M[0])
        A = [[0] * (n + 1) for _ in range(m + 1)]
        good = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                A[i + 1][j + 1] = A[i + 1][j] + A[i][j + 1] - A[i][j] + (1 - M[i][j])
                if i + 1 >= h and j + 1 >= w:
                    x, y = i + 1 - h, j + 1 -w
                    if A[i + 1][j + 1] - A[x][j + 1] - A[i + 1][y] + A[x][y] == w * h:
                        good[i][j] += 1
                        
        B = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                B[i + 1][j + 1] = B[i + 1][j] + B[i][j + 1] - B[i][j] + good[i][j]
        for i in range(m):
            for j in range(n):
                x, y = min(i + h, m), min(j + w, n)
                if M[i][j] == 0 and B[x][y] - B[i][y] - B[x][j] + B[i][j] == 0:
                    return False
        return True