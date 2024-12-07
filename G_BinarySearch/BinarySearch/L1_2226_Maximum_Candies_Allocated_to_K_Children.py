""" https://leetcode.com/problems/maximum-candies-allocated-to-k-children/
"""


class Solution:
    def maximumCandies(self, A: List[int], k: int) -> int:
        def fn(m):
            if m == 0:
                return False
            ans = 0
            for x in A:
                ans += x // m
            return ans < k

        l, r = 0, sum(A) // k + 1
        while l < r:
            m = (l + r) // 2
            if fn(m):
                r = m
            else:
                l = m + 1
        return l - 1
