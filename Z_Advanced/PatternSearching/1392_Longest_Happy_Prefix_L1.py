""" https://leetcode.com/problems/longest-happy-prefix/
longest happy prefix essentially is longest prefix suffux(lps)
"""
class Solution:
    def longestPrefix(self, s: str) -> str:
        i = 0
        lps = [0] * len(s)
        for j in range(1, len(s)):
            while s[i]!=s[j] and i: i = lps[i-1]
            if s[i]==s[j]:
                i += 1
                lps[j] = i
        return s[:lps[-1]]