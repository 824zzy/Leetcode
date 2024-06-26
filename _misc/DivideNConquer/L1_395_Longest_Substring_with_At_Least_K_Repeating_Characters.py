""" https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
Essentially it is a divide and conquer problem: divide the string by characters which frequency lower than k.
"""
from header import *


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def dfs(s):
            if len(s) < k:
                return 0
            freq = Counter(s)
            if min(freq.values()) < k:
                m = min(freq, key=freq.get)
                return max(dfs(ss) for ss in s.split(m))
            else:
                return len(s)

        return dfs(s)
