""" https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/
Note that in python, 0.1+0.2 = 0.30000000000000004 != 0.3,
thus in order to compute slope, we can either avoid float calculation(division) or use high precision fractions.Fraction
"""
# from god lee: avoid float calculation by mutiplication rather than division
from fractions import Fraction


class Solution:
    def minimumLines(self, A: List[List[int]]) -> int:
        n = len(A)
        res = n - 1
        A.sort()
        for i in range(1, n - 1):
            a, b, c = A[i - 1], A[i], A[i + 1]
            if (b[0] - a[0]) * (c[1] - b[1]) == (c[0] - b[0]) * (b[1] - a[1]):
                res -= 1
        return res


# avoid float calculation by add all slopes to a set


class Solution:
    def minimumLines(self, A: List[List[int]]) -> int:
        A.sort(key=lambda x: (x[0], -x[1]))
        line = set()
        for i in range(len(A) - 1):
            x1, y1 = A[i][0], A[i][1]
            x2, y2 = A[i + 1][0], A[i + 1][1]
            k = (y1 - y2) / (x1 - x2)
            b = (x1 * y2 - x2 * y1) / (x1 - x2)
            line.add((k, b))
        return len(line)


# use Fraction for high precision float calculation


class Solution:
    def minimumLines(self, A: List[List[int]]) -> int:
        ans = 0
        A = [
            Fraction(A[i + 1][1] - A[i][1]) / Fraction(A[i + 1][0] - A[i][0])
            for i in range(len(A) - 1)
        ]
        for i in range(len(A) - 1):
            if A[i] != A[i + 1]:
                ans += 1
        return ans + (len(A) > 0)
