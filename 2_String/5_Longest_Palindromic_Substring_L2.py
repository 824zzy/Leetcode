""" Best solution with expand pointers
Especially for the palindrome questions
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s==s[::-1]:
            return s
        
        l, r = 0, 0
        for i in range(len(s)):
            # check odd and even
            l, r = max((l, r), self.expand(s, i, i), self.expand(s, i, i+1),
                       key=lambda x: x[1]-x[0])
        return s[l:r]
    
    def expand(self, s: str, l: int, r:int) -> int:
        while l>=0 and r<len(s) and s[l]==s[r]:
            l, r = l-1, r+1
        return l+1, r