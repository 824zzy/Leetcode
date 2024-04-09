""" https://leetcode.com/problems/tallest-billboard/
This is a special 01 knapsack that we have three choice for each item:
1. skip the rod
2. add the rod to left steel
3. add the rod to right steel
"""
from header import *


class Solution:
    def tallestBillboard(self, A: List[int]) -> int:
        @cache
        def dp(i, diff):
            if i == len(A):
                return 0 if diff == 0 else -inf
            # skip
            ans = dp(i + 1, diff)
            # add to left steel
            ans = max(ans, A[i] + dp(i + 1, diff + A[i]))
            # add to right steel
            ans = max(ans, A[i] + dp(i + 1, diff - A[i]))
            return ans

        return dp(0, 0) // 2


# TLE
class Solution:
    def tallestBillboard(self, A: List[int]) -> int:
        A.sort()
        self.ans = 0

        @cache
        def dp(i, sm1, sm2):
            if i == len(A):
                if sm1 == sm2:
                    self.ans = max(self.ans, sm1)
                return
            # skip
            dp(i + 1, sm1, sm2)
            # assign to sm1
            dp(i + 1, sm1 + A[i], sm2)
            # assign to sm2
            dp(i + 1, sm1, sm2 + A[i])

        dp(0, 0, 0)
        return self.ans
