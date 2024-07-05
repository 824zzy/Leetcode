""" https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/
1. 2 <= nums.length == n <= 1000 ==> O(n^2)
2. dp
"""
from header import *


class Solution:
    def maximumJumps(self, A: List[int], t: int) -> int:
        n = len(A)

        @cache
        def dp(i):
            if i == n - 1:
                return 0
            ans = -inf
            for j in range(i + 1, n):
                if abs(A[i] - A[j]) <= t:
                    ans = max(ans, dp(j) + 1)
            return ans

        ans = dp(0)
        return ans if ans != -inf else -1


"""
[1,3,6,4,1,2]
2
[1,3,6,4,1,2]
3
[1,3,6,4,1,2]
0
"""
