""" https://leetcode.com/problems/valid-palindrome-ii/
two pointers + categorization

1. use two pointers to find the first different character pairs
2. check if any one of the two conditions(A[l:r], A[l+1:r+1]) is valid palindrome
"""
from header import *


class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                # delete left
                if s[l + 1:r + 1] == s[l + 1:r + 1][::-1]:
                    return True
                # delete right
                elif s[l:r] == s[l:r][::-1]:
                    return True
                else:
                    return False
        return True
