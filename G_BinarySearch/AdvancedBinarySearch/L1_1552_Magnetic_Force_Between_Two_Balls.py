""" https://leetcode.com/problems/magnetic-force-between-two-balls/
a naive sliding window inside binary search
"""


class Solution:
    def maxDistance(self, A: List[int], b: int) -> int:
        def fn(m, b):
            i = 0
            for j in range(1, len(A)):
                if A[j] - A[i] > m:
                    i, b = j, b - 1
            return b >= 0

        A.sort()
        l, r = 1, A[-1] - A[0]
        b -= 2
        while l < r:
            m = (l + r) // 2
            if fn(m, b):
                r = m
            else:
                l = m + 1
        return l
