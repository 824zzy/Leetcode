""" https://leetcode.com/problems/is-subsequence/
"""
from header import *

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        @cache
        def dp(i, j):
            if i==len(s): return True
            elif j==len(t): return False
            
            if s[i]==t[j]: return dp(i+1, j+1)
            else: return dp(i, j+1)
            
        return dp(0, 0)
    

# two pointers
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for j in range(len(t)):
            if i+1<len(s) and s[i]==t[j]: i += 1
        return i==len(s)