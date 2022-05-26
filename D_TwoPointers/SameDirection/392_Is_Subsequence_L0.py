""" https://leetcode.com/problems/is-subsequence/
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for j in range(len(t)):
            if i+1<=len(s) and s[i]==t[j]: i += 1
        return i==len(s)