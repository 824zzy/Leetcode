""" Special two pointer for checking if two characters are equal.
Check from left and right at the same time until the first different pair.
"""
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l<r and s[l]==s[r]:
            l += 1
            r -= 1
        s = s[l:r+1] 
        return s[1:]==s[1:][::-1] or s[:-1]==s[:-1][::-1]