""" https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
sliding window with hash table
"""
from header import *


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        cnt = Counter()
        i = 0
        res = 0
        for j in range(len(s)):
            cnt[s[j]] += 1
            while len(cnt) > 2:
                cnt[s[i]] -= 1
                if cnt[s[i]] == 0:
                    cnt.pop(s[i])
                i += 1
            res = max(res, j - i + 1)
        return res


"""
"eceba"
"ccaabbb"
"""
