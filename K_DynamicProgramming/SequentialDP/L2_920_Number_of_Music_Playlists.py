""" https://leetcode.com/problems/number-of-music-playlists/
sequential dp + math (factorial)

All it matters is the number of sones that has already appeared in the list (i.e. x here).
There are two cases:
1. If x<n, we can add a new song to the list. There are n-x songs that can be added.
2. If x>=k, we can add an old song to the list. There are x-k songs that can be added.
"""
from header import *


class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        @cache
        def dp(i, x):
            if i == goal:
                return x == n
            ans = 0
            if x < n:  # new song
                ans += (n - x) * dp(i + 1, x + 1)
            if k < x:  # old song
                ans += (x - k) * dp(i + 1, x)
            return ans % (10 ** 9 + 7)

        return dp(0, 0)
