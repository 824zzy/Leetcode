""" https://leetcode.com/problems/length-of-the-longest-valid-substring/
1 <= forbidden[i].length <= 10 ==> brute force to check all substrings of length 10
"""
from header import *


class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbidden = set(forbidden)
        ans = 0
        i = 0
        for j in range(len(word)):
            for ii in reversed(range(max(j - 10, i), j + 1)):
                if word[ii:j + 1] in forbidden:
                    i = ii + 1
                    break
            ans = max(ans, j - i + 1)
        return ans
