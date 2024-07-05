""" https://leetcode.com/problems/string-compression-ii/
idx: Index of the current symbol
prev: The last symbol we have in our compression
cnt: The number of lastChar we have considered
k: The number of symbols we are still allowed to delete
"""
from header import *


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        def rle(x):
            if x <= 1:
                return x
            else:
                return int(log10(x)) + 2

        @cache
        def dp(i, k, pre, cnt):
            if k < 0:
                return inf
            if i == len(s):
                return 0
            ans = dp(i + 1, k - 1, pre, cnt)  # delete current char
            if pre == s[i]:
                ans = min(ans, dp(i + 1, k, s[i], cnt + 1) + rle(cnt + 1) - rle(cnt))
            else:
                ans = min(ans, dp(i + 1, k, s[i], 1) + 1)
            return ans

        return dp(0, k, "", 0)


"""
"aaabcccd"
2
"aabbaa"
2
"aaaaaaaaaaa"
0
"abc"
2
"bbabbbabbbbcbb"
4
"""
