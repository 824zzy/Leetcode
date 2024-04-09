""" https://leetcode.com/problems/maximal-square/
2D prefix sum + binary search
"""


class Solution:
    def maximalSquare(self, A: List[List[str]]) -> int:
        # compute 2D prefix sum
        m, n = len(A), len(A[0])
        prefix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = int(A[i][j]) + prefix[i][j + 1] + \
                    prefix[i + 1][j] - prefix[i][j]

        # binary search to find maximum area
        def fn(x):
            for i in range(x - 1, m):
                for j in range(x - 1, n):
                    if prefix[i + 1][j + 1] - prefix[i + 1 - x][j + 1] - \
                            prefix[i + 1][j + 1 - x] + prefix[i + 1 - x][j + 1 - x] >= x * x:
                        return True
            return False

        l, r = 1, max(m, n) + 1
        while l < r:
            mid = (l + r) // 2
            if not fn(mid):
                r = mid
            else:
                l = mid + 1
        return (l - 1)**2
