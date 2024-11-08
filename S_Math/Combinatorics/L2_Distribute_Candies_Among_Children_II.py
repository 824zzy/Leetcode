""" https://leetcode.com/problems/distribute-candies-among-children-ii/
first children: 0 <= i <= min(limit, n)
second children: 0 <= j <= limit and i+j <= n ===> j <= n-i
third children: 0 <= n-i-j <= limit ===> n-i-limit <= j

===> n-i-limit <= j <= n-i
===> max(0, n-i-limit) <= j <= min(n-i, limit)
"""


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        for i in range(min(limit, n) + 1):
            rem = n - i  # n-i remained candies
            mx = min(limit, rem)  # upper bound
            mn = max(0, rem - limit)  # lower bound
            if mn <= mx:
                ans += mx - mn + 1
        return ans
