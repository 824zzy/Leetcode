""" https://leetcode.com/problems/implement-strstr/
kmp template
"""
class Solution:
    def strStr(self, s: str, p: str) -> int:
        if not p: return 0
        def getLPS(s):
            i = 0
            lps = [0] * len(s)
            for j in range(1, len(s)):
                while s[j] != s[i] and i: i = lps[i-1]
                if s[j] == s[i]: i += 1
                lps[j] = i
            return lps
        
        lps = getLPS(p)
        i = 0
        for j in range(len(s)):
            while s[j]!=p[i] and i: i = lps[i-1]
            if s[j]==p[i]: i += 1
            if i==len(p): return j-len(p)+1
        return -1