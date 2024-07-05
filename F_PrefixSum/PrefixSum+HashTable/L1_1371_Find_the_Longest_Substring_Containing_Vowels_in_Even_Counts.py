""" https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/
bit mask + prefix sum + hash table

1. Represent the counts (odd or even) of vowels with a bitmask.
2. presum[j] should be the same as presum[i]
"""
from header import *


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        mp = {"a": 0, "e": 1, "i": 2, "o": 3, "u": 4}
        cnt = Counter()
        cnt[0] = -1
        ans = pre = 0
        for i, c in enumerate(s):
            if c in mp:
                pre ^= 1 << (1 << mp[c])
            if pre in cnt:
                ans = max(ans, i - cnt[pre])
            cnt.setdefault(pre, i)
        return ans
