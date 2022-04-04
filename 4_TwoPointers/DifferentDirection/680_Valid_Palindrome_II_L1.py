""" https://leetcode.com/problems/valid-palindrome-ii/
1. use two pointers to find the first different character pairs
2. check if any one of the two conditions(A[l:r], A[l+1:r+1]) is valid palindrome
"""
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l<r and s[l]==s[r]:
            l, r = l+1, r-1
        else: return s[l+1:r+1]==s[l+1:r+1][::-1] or s[l:r]==s[l:r][::-1]