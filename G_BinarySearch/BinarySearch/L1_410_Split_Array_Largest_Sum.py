""" https://leetcode.com/problems/split-array-largest-sum/
the same as 1011
Use binary search to check if the array can be splitted as multiple subarray whose sum is m.
Note that the lower bound is max(A)
"""


class Solution:
    def splitArray(self, A: List[int], n: int) -> int:
        def fn(m, n):
            _m = m
            for x in A:
                if _m - x >= 0:
                    _m -= x
                else:
                    _m, n = m - x, n - 1
            return n > 0

        l, r = max(A), sum(A)
        while l < r:
            m = (l + r) // 2
            if fn(m, n):
                r = m
            else:
                l = m + 1
        return l
