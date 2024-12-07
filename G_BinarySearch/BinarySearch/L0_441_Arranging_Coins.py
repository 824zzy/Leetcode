""" https://leetcode.com/problems/arranging-coins/
find complete rows using middle number through m*(m+1)//2
"""


class Solution:
    def arrangeCoins(self, n: int) -> int:
        def fn(m):
            if m * (m + 1) // 2 > n:
                return True
            else:
                return False

        l, r = 0, n + 1
        while l < r:
            m = (l + r) // 2
            if fn(m):
                r = m
            else:
                l = m + 1
        return l - 1
