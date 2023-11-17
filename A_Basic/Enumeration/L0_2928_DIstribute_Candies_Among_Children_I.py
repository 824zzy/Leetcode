""" https://leetcode.com/problems/distribute-candies-among-children-i/
enumerate on first two children
"""
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        for i in range(min(n, limit)+1):
            for j in range(min(n-i, limit) + 1):
                k = n-i-j
                if 0 <= k <= limit:
                    ans += 1
        return ans