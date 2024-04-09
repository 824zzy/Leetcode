""" https://leetcode.com/problems/rotate-string/
check if p in s+s using KMP
"""


class Solution:
    def rotateString(self, s: str, p: str) -> bool:
        if len(s) != len(p):
            return False

        def getLPS(s):
            i = 0
            lps = [0] * len(s)
            for j in range(1, len(s)):
                while s[j] != s[i] and i:
                    i = lps[i - 1]
                if s[j] == s[i]:
                    i += 1
                lps[j] = i
            return lps

        lps = getLPS(p)
        i = 0
        s *= 2
        for j in range(len(s)):
            while s[j] != p[i] and i:
                i = lps[i - 1]
            if s[j] == p[i]:
                i += 1
            if i == len(p):
                return True
        return False
