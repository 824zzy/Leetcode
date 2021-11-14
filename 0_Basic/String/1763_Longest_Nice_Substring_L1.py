""" Brute Force
"""
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans = ""
        def check(sub):
            chars = set(sub)
            for c in chars:
                if c.lower() not in sub or c.upper() not in sub:
                    return False
            return True
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                if len(s[i:j+1])>len(ans):
                    if check(s[i:j+1]): ans = s[i:j+1]
        return ans