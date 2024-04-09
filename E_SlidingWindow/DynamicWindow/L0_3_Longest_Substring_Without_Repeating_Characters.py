""" https://leetcode.com/problems/longest-substring-without-repeating-characters/
Use a dictionary seen as a sliding window
"""
from header import *


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt = Counter()
        ans = 0
        i = 0
        for j, c in enumerate(s):
            cnt[c] += 1
            while cnt[c] > 1:
                cnt[s[i]] -= 1
                i += 1
            ans = max(ans, j - i + 1)
        return ans
