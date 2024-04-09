""" https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/
prefix sum + dp

1. prefix sum for reducing time complexity
2. use dp to find the max value of k coins from piles
"""
from header import *


class Solution:
    def maxValueOfCoins(self, A: List[List[int]], k: int) -> int:
        pre_sum = [list(accumulate(x, initial=0)) for x in A]

        @cache
        def dp(i, k):
            if k == 0 or i == len(A):
                return 0
            ans = 0
            for kk in range(min(len(pre_sum[i]), k + 1)):
                ans = max(ans, pre_sum[i][kk] + dp(i + 1, k - kk))
            return ans

        return dp(0, k)


"""
[[1,100,3],[7,8,9]]
2
[[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]]
7
"""
