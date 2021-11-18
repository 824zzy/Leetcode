""" L1: https://leetcode.com/problems/arranging-coins/
find complete rows using middle number through m*(m+1)//2
"""
class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n
        while l<=r:
            m = (l+r)//2
            if m*(m+1)//2<=n: l = m + 1
            else: r = m - 1
        return r