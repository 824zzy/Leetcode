""" https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/description/
simply find the longest subsequence prefix of t in s
"""


class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        for j in range(len(s)):
            if i == len(t):
                return 0
            if s[j] == t[i]:
                i += 1
        return len(t) - i


""" 4 0 5 2
"coaching"
"coding"
"abcde"
"a"
"z"
"abcde"
"vrykt"
"rkge"
"""
