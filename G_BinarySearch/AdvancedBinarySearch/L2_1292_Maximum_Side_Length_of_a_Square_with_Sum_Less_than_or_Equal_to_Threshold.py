""" https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/
comprehensive problem: 2D prefix sum + Sentinel binaery search
"""


class Solution:
    def maxSideLength(self, A: List[List[int]], t: int) -> int:
        m, n = len(A), len(A[0])
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = A[i][j] + prefix[i][j + 1] + \
                    prefix[i + 1][j] - prefix[i][j]

        def fn(x):
            for i in range(m - x + 1):
                for j in range(n - x + 1):
                    if (prefix[i + x][j + x] - prefix[i + x][j] -
                            prefix[i][j + x] + prefix[i][j]) <= t:
                        return True
            return False

        l, r = 0, min(m, n) + 1
        while l < r:
            mid = (l + r) // 2
            if not fn(mid):
                r = mid
            else:
                l = mid + 1
        return l - 1
