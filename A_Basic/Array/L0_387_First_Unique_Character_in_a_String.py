""" https://leetcode.com/problems/first-unique-character-in-a-string/
counting through Counter
"""
from header import *
class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter(s)
        for i, c in enumerate(s):
            if cnt[c] == 1:
                return i
        return -1