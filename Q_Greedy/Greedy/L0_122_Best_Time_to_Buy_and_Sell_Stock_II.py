""" https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
since we are allowed to do as much transactions as we can, so greedily sum up all positive gains.
"""


class Solution:
    def maxProfit(self, A: List[int]) -> int:
        ans = 0
        for i in range(len(A) - 1):
            if A[i] < A[i + 1]:
                ans += A[i + 1] - A[i]
        return ans
