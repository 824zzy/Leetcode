""" https://leetcode.com/problems/unique-substrings-with-equal-digit-frequency/
TODO: add rolling hash solution
"""
from header import *

# suboptimal brute force solution, time complexity O(n^3)
class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        ans = 0
        seen = set()
        for i in range(len(s)):
            cnt = Counter()
            for j in range(i, len(s)):
                cnt[s[j]] += 1
                if len(set(cnt.values()))==1:
                    if s[i:j+1] not in seen:
                        ans += 1
                        seen.add(s[i:j+1])
        return ans