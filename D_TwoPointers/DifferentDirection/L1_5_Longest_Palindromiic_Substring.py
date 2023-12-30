""" https://leetcode.com/problems/longest-palindromic-substring/
the same as 647

to cover odd and even cases: 
1. ranging from 0 to 2*len(s)-1
2. l = i//2, r = (i+1)//2 
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        for i in range(2*len(s)-1):
            l, r = i//2, (i+1)//2
            while 0<=l<=r<len(s) and s[l]==s[r]:
                l, r = l-1, r+1
            ans = max(ans, s[l+1:r], key=len)
        return ans
    

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            while 0<=l<=r<len(s) and s[l]==s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
            
        ans = ''
        for i in range(len(s)):
            ans = max(ans, expand(i, i), expand(i, i+1), key=len)
        return ans