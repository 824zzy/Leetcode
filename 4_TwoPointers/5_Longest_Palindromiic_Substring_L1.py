""" https://leetcode.com/problems/longest-palindromic-substring/
lo = i//2, hi = (i+1)//2 to cover odd and even cases
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