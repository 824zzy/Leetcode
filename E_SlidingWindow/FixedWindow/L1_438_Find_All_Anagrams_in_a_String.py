""" https://leetcode.com/problems/find-all-anagrams-in-a-string/
use a fixed sliding window and a Counter to record p's frequency
when Counter values equal to p's frequency, append the start index of the window
"""
from header import *


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        t = Counter(p)
        cnt = Counter(s[: len(p)])
        if t == cnt:
            ans.append(0)

        for i in range(len(p), len(s)):
            cnt[s[i - len(p)]] -= 1
            cnt[s[i]] += 1
            if t == cnt:
                ans.append(i - len(p) + 1)
        return ans
